#! /usr/bin/env python
import rospy
from ast import literal_eval
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from mavros_msgs import WaypointReached
import os
import socket

class Warden(object):

    def __init__(self):
        self.reached = ""
        # Subscriber to get Tank Status
        self.stat = rospy.Subscriber('~mission/reached', WaypointReached, self.getStatus)
        # Navigation
        self.captured = rospy.Publisher('/captured', String)
        self.correctedpoint = rospy.Publisher('/gpsTarget', String, queue_size=0)
        rospy.Subscriber('/gpsTarget', String, self.getCoordinates)
        self.capture()

    # Subscriber callback for Way-point verification
    def getStatus(self, msg):
        if msg.data.wp_seq == 1:
            self.reached = 1

    def getCoordinates(self, msg):
        if msg.data != "-1":
            self.location = (literal_eval(msg.data)).position

    # Function to send capture message to the robotic arms and Publish data to the navigator to return.
    def capture(self):
        while not rospy.is_shutdown():
            rospy.loginfo("Standing By")
            if (self.reached != "" and self.reached == 1):
                # Captured
                UDP_IP = "192.168.188.60"
                UDP_PORT = 9000
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
                sock.bind((UDP_IP, UDP_PORT))
                data = ["","","","",""]
                while data[4] == "":
                    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
                    #right
                    if data[1] != "":
                        self.correctedpoint.publish((self.location.lattitude) + (self.location.longitude+0.00005))
                    #left
                    if data[3] != "":
                        self.correctedpoint.publish((self.location.lattitude) + (self.location.longitude - 0.00005))
                    # front
                    if data[2] != "":
                        self.correctedpoint.publish((self.location.lattitude + 0.00005) + (self.location.longitude))

                os.system("./capture.sh")
                self.captured.publish("1")
                break


if __name__ == "__main__":
    rospy.init_node('Warden', log_level=rospy.INFO)
    go_home_object = Warden()
    rospy.spin()

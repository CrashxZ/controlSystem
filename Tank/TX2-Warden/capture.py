#! /usr/bin/env python
import rospy
from ast import literal_eval
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from mavros_msgs import WaypointReached
import os


class Warden(object):

    def __init__(self):
        self.reached = ""
        # Subscriber to get Tank Status
        self.stat = rospy.Subscriber('~mission/reached', WaypointReached, self.getStatus)
        # Navigation
        self.captured = rospy.Publisher('/captured', String)
        self.capture()

    # Subscriber callback for Way-point verification
    def getStatus(self, msg):
        if msg.data.wp_seq == 1:
            self.reached = 1

    # Function to send capture message to the robotic arms and Publish data to the navigator to return.
    def capture(self):
        while not rospy.is_shutdown():
            rospy.loginfo("Standing By")
            if (self.target != "" and self.reached == 1):
                # Captured
                os.system("./capture.sh")
                self.captured.publish("1")
                break


if __name__ == "__main__":
    rospy.init_node('Warden', log_level=rospy.INFO)
    go_home_object = Warden()
    rospy.spin()

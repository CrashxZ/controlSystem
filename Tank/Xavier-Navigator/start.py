#! /usr/bin/env python
import rospy
from ast import literal_eval
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from mavros_msgs import WaypointReached
import os


class navigate(object):

    def __init__(self):
        self.target = ""
        self.start = 0
        self.back = 0
        # Navigation Return
        rospy.Subscriber('/captured', String,self.getReturnCommand)
        #GPS Target
        rospy.Subscriber('/gpsTarget', String, self.getCoordinates)
        #Navigation Start
        rospy.Subscriber('/navigator', String, self.getStartCommand)

        self.goTarget()
        self.returnTarget()

    def getStartCommand(self, msg):
        if msg.data == "1":
            self.start = 1

    def getReturnCommand(self, msg):
        if msg.data == "1":
            self.back = 1

    def getCoordinates(self, msg):
        if msg.data != "-1":
            self.target = (literal_eval(msg.data)).position

    # Function to send gps coordinates to the pixhawk
    def goTarget(self):
        while not rospy.is_shutdown():
            rospy.loginfo("Standing By")
            if (self.start == 1):
                # start navigation
                #TODO: Delay 10 mins
                #TODO: ARM AND SEND GPS COORDINATES TO THE PIXHAWK
                os.system("sleep 600;./navigate.sh "+ self.target.lattitude +" "+self.target.longitude)

    def returnTarget(self):
        while not rospy.is_shutdown():
            if (self.back == 1):
                rospy.loginfo("Returning")
                # return navigation
                #TODO: ARM AND SEND GPS COORDINATES TO THE PIXHAWK
                os.system("")


if __name__ == "__main__":
    rospy.init_node('tank_nav', log_level=rospy.INFO)
    go_home_object = navigate()
    rospy.spin()
#! /usr/bin/env python
import rospy
from ast import literal_eval
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import os


class startnav(object):

    def __init__(self):
        self.navigator = rospy.Publisher('/navigator', String)
        self.startnav()



    # Function to Publish data to the publisher
    def startnav(self):
        while not rospy.is_shutdown():
            self.navigator.publish("1")



if __name__ == "__main__":
    rospy.init_node('startnav', log_level=rospy.INFO)
    go_home_object = startnav()
    rospy.spin()

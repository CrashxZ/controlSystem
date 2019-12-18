#! /usr/bin/env python
import serial
import os
import rospy
import numpy as np
import json
import importlib
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Pose, PoseStamped, Point, PointStamped
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import time


class gpsPublisher(object):

    def __init__(self):
        # Publisher to broadcast GPS coordinates in ROS
        self.setpoint = rospy.Publisher('/gpsTarget', String, queue_size=0)
        self.gps = serial.Serial("/dev/ttyTHS0", baudrate=57600, timeout=1)



    # Function to read the GPS Coordinates from 3D Radio and Publish it in ROS
    def gpsPublish(self):
        while gps.is_open:
            position = gps.readline()
            rospy.loginfo(position)
            self.gps.publish(position)


if __name__ == "__main__":
    rospy.init_node('gps_publisher', log_level=rospy.INFO)
    go_home_object = gpsPublisher()
    rospy.spin()
#!/bin/bash

# ROS Slave - Tank Jetson TX2 - 3D Radio
# HOST - 192.168.188.101
export ROS_HOSTNAME=192.168.188.101
export ROS_MASTER_URI=http://192.168.188.100:11311/
export ROS_MASTER_IP=192.168.188.100

cd /radio
source devel/setup.bash
rosrun ugps gpsPublisher.py
$SHELL
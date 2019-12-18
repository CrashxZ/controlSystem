#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Warden Arm Servo Control
# HOST - 192.168.188.60
export ROS_HOSTNAME=192.168.188.60
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

cd /warden
source devel/setup.bash
rosrun warden capture.py
$SHELL

#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Terminator
# HOST - 192.168.188.150
export ROS_HOSTNAME=192.168.188.150
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

cd /terminator
source devel/setup.bash
rosrun terminator terminate.py
$SHELL


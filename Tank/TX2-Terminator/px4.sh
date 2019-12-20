#!/bin/bash

# ROS Master II - Tank Jetson TX2 - Terminator
# HOST - 192.168.188.150
export ROS_HOSTNAME=192.168.188.150
export ROS_MASTER_URI=http://192.168.188.150:11311/
export ROS_MASTER_IP=192.168.188.150

cd $HOME/mavros
source devel/setup.bash
roslaunch mavros px4.launch
$SHELL
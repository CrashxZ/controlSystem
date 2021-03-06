#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Navigator
# HOST - 192.168.188.100
export ROS_HOSTNAME=192.168.188.100
export ROS_MASTER_URI=http://192.168.188.100:11311/
export ROS_MASTER_IP=192.168.188.100

cd $HOME/mavros
source devel/setup.bash
roslaunch mavros px4.launch
$SHELL
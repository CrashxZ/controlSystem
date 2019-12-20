#!/bin/bash

# ROS Master II- Tank Jetson TX2 - Navigator
# HOST - 192.168.188.100
export ROS_HOSTNAME=192.168.188.100
export ROS_MASTER_URI=http://192.168.188.100:11311/
export ROS_MASTER_IP=192.168.188.100

export DISPLAY=:0.0
gnome-terminal -- bash -c "./px4.sh"


cd $HOME/navigator
source devel/setup.bash
rosrun navigator start.py
$SHELL


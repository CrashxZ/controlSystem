#!/bin/bash

# ROS Master - UAV Jetson Xavier
# HOST - 192.168.188.8
export ROS_HOSTNAME=192.168.188.8
export ROS_MASTER_URI=http://192.168.188.8:11311/
export ROS_MASTER_IP=192.168.188.8

# shellcheck disable=SC2164
cd $HOME/hunter/droneHunter/build
./DroneHunter
$SHELL

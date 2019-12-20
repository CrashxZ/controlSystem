#!/bin/bash

# ROS Master II- Tank Jetson TX2 - Navigator
# HOST - 192.168.188.100
export ROS_HOSTNAME=192.168.188.100
export ROS_MASTER_URI=http://192.168.188.100:11311/
export ROS_MASTER_IP=192.168.188.100


lattitude=$1
longitude=$2

#send global position to pixhawk to navigate
rosservice call /mavros/mission/push "start_index:0 waypoints:- {frame: 0, command: 0, is_current: false, autocontinue: false, param1: 0.0, param2: 0.0, param3: 0.0, param4:0.0 , x_lat: $lattitude, y_long : $longitude, z_alt: 0.1"
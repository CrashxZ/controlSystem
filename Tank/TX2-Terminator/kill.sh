#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Terminator
# HOST - 192.168.188.150
export ROS_HOSTNAME=192.168.188.150
export ROS_MASTER_URI=http://192.168.188.150:11311/
export ROS_MASTER_IP=192.168.188.150
export DISPLAY=:0.0
gnome-terminal -- bash -c "./px4.sh"
#set navvigator to 1
gnome-terminal -- bash -c "./navflag.sh"


cd $HOME/mavros
source devel/setup.bash
roslaunch mavros mavsafety -v arm
# PWM signals to override rc channels / AUX Output to the Terminator 150 Relay
rostopic pub -1 /mavros/rc/override mavros_msgs/OverrideRCIn '[2000, 1500, 1500, 1500, 1500, 1500, 1500, 1500]'

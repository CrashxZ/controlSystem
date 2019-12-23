#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Warden
# HOST - 192.168.188.60
export ROS_HOSTNAME=192.168.188.60
export ROS_MASTER_URI=http://192.168.188.60:11311/
export ROS_MASTER_IP=192.168.188.60
export DISPLAY=:0.0
gnome-terminal -- bash -c "./px4.sh"

sleep 20
cd $HOME/mavros
source devel/setup.bash
roslaunch mavros mavsafety -v arm
# PWM signals to override rc channels / AUX Output to the arm servos
rostopic pub -1 /mavros/rc/override mavros_msgs/OverrideRCIn '[2000, 1500, 1500, 1500, 1500, 1500, 1500, 1500]'
sleep 5
rostopic pub -1 /mavros/rc/override mavros_msgs/OverrideRCIn '[2000, 2000, 1500, 1500, 1500, 1500, 1500, 1500]'
sleep 5
rostopic pub -1 /mavros/rc/override mavros_msgs/OverrideRCIn '[1000, 1500, 1500, 1500, 1500, 1500, 1500, 1500]'
#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Warden
# HOST - 192.168.188.60

cd $HOME/mavros
source devel/setup.bash
mavsafety -v arm
# PWM signals to override rc channels / AUX Output to the arm servos
#!/bin/bash

# ROS Slave - Tank Jetson TX2 - Terminator
# HOST - 192.168.188.150

cd $HOME/mavros
source devel/setup.bash
mavsafety -v arm
# PWM signals to override rc channels / AUX Output to the Terminator 150 Relay


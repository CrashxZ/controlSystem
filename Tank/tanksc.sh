#!/bin/bash
# ROS launcher
#connection to TANK Computers
export DISPLAY=:0.0

#Tank- Navigatior
gnome-terminal -- bash -c "spawn ssh nvidia@192.168.188.100;expect
"password:";sleep 1;send "nvidia\r"; sleep 5; cd $HOME\navigator;
./init.sh"

#Tank- Terminator
gnome-terminal -- bash -c "spawn ssh nvidia@192.168.188.150;expect
"password:";sleep 1;send "nvidia\r"; sleep 5; cd $HOME\terminator;
./init.sh"

#Tank- Radio
gnome-terminal -- bash -c "spawn ssh nvidia@192.168.188.101;expect
"password:";sleep 1;send "nvidia\r"; sleep 5; cd $HOME\radio;
./init.sh"

#Tank- Warden Arm Servo Control
gnome-terminal -- bash -c "spawn ssh nvidia@192.168.188.60;expect
"password:";sleep 1;send "nvidia\r"; sleep 5; cd $HOME\warden;
./init.sh"

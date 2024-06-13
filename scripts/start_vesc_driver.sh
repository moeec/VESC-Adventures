#!/bin/sh

# launch vesc_driver_node.launch

xterm -e "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_node.launch " & 

sleep 15

# launch gmapping_demo.launch to perform slam_gmapping

xterm -hold -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_nodelet.launch "

#!/bin/sh

# Load Some Parameters for Ackermann

rosparam set /speed_to_erpm_gain 0.5
rosparam set /speed_to_erpm_offset 0.2
rosparam set /steering_angle_to_servo_gain  0.2
rosparam set /steering_angle_to_servo_offset 0.1
rosparam set /wheelbase 0.8


# launch vesc_driver_node.launch

xterm -e "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_node.launch " & 

sleep 5

# launch vesc_driver_nodelet 

xterm -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_nodelet.launch " &


# launch vesc_driver_nodelet 

xterm -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_ackermann vesc_to_odom_node.launch "

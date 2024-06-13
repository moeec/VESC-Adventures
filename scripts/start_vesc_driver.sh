#!/bin/sh

# Load Some Parameters for Ackermann

# erpm (electrical rpm) = speed_to_erpm_gain * speed (meters / second) + speed_to_erpm_offset

rosparam set /speed_to_erpm_gain 4614
rosparam set /speed_to_erpm_offset 0.0

# Set gains for converting acceleration to current and brake control values

rosparam set /accel_to_current_gain 100
rosparam set /accel_to_brake_gain -80

# servo value (0 to 1) =  steering_angle_to_servo_gain * steering angle (radians) + steering_angle_to_servo_offset

rosparam set /steering_angle_to_servo_gain  -1.2135
rosparam set /steering_angle_to_servo_offset 0.5304


rosparam set /wheelbase .25


rosparam set /tachometer_ticks_to_meters_gain: 0.00225
# servo smoother - limits rotation speed and smooths anything above limit

rosparam set /max_servo_speed: 3.2 # radians/second
rosparam set /servo_smoother_rate 75.0 # messages/sec

# servo smoother - limits acceleration and smooths anything above limit

rosparam set /max_acceleration 2.5 # meters/second^2
rosparam set /throttle_smoother_rate 75.0 # messages/sec



# launch vesc_driver_node.launch

xterm -e "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_node.launch " & 

sleep 5

# launch vesc_driver_nodelet 

xterm -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_driver vesc_driver_nodelet.launch " &


# launch vvesc_to_odom_node.launch

xterm -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_ackermann vesc_to_odom_node.launch "


# launch ackermann_to_vesc_node.launch

xterm -e  "cd $(pwd)/../..;
source devel/setup.bash;
roslaunch vesc_ackermann ackermann_to_vesc_node.launch

Notes for ROS1 Version:

mwesi@mwesi-developer:~/vesc_ws$ roslaunch vesc_driver vesc_driver_node.launch
... logging to /home/mwesi/.ros/log/595f2c02-2832-11ef-b885-48b02dec0a12/roslaunch-mwesi-developer-22079.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://mwesi-developer:46059/

SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0
 * /vesc_driver_node/port: /dev/ttyACM0

NODES
  /
    vesc_driver_node (vesc_driver/vesc_driver_node)

auto-starting new master
process[master]: started with pid [22087]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to 595f2c02-2832-11ef-b885-48b02dec0a12
process[rosout-1]: started with pid [22098]
started core service [/rosout]
process[vesc_driver_node-2]: started with pid [22101]
[ INFO] [1718138219.557442526]: Connected to VESC with firmware version 6.2


mwesi@mwesi-developer:~/vesc_ws$ ls
build  devel  src
mwesi@mwesi-developer:~/vesc_ws$ ls
build  devel  src
mwesi@mwesi-developer:~/vesc_ws$ ls /dev/tty*
/dev/tty    /dev/tty15  /dev/tty22  /dev/tty3   /dev/tty37  /dev/tty44  /dev/tty51  /dev/tty59  /dev/tty9     /dev/ttyp4  /dev/ttypc  /dev/ttyTCU0
/dev/tty0   /dev/tty16  /dev/tty23  /dev/tty30  /dev/tty38  /dev/tty45  /dev/tty52  /dev/tty6   /dev/ttyACM0  /dev/ttyp5  /dev/ttypd  /dev/ttyTHS0
/dev/tty1   /dev/tty17  /dev/tty24  /dev/tty31  /dev/tty39  /dev/tty46  /dev/tty53  /dev/tty60  /dev/ttyAMA0  /dev/ttyp6  /dev/ttype  /dev/ttyTHS3
/dev/tty10  /dev/tty18  /dev/tty25  /dev/tty32  /dev/tty4   /dev/tty47  /dev/tty54  /dev/tty61  /dev/ttyGS0   /dev/ttyp7  /dev/ttypf  /dev/ttyTHS4
/dev/tty11  /dev/tty19  /dev/tty26  /dev/tty33  /dev/tty40  /dev/tty48  /dev/tty55  /dev/tty62  /dev/ttyp0    /dev/ttyp8  /dev/ttyS0
/dev/tty12  /dev/tty2   /dev/tty27  /dev/tty34  /dev/tty41  /dev/tty49  /dev/tty56  /dev/tty63  /dev/ttyp1    /dev/ttyp9  /dev/ttyS1
/dev/tty13  /dev/tty20  /dev/tty28  /dev/tty35  /dev/tty42  /dev/tty5   /dev/tty57  /dev/tty7   /dev/ttyp2    /dev/ttypa  /dev/ttyS2
/dev/tty14  /dev/tty21  /dev/tty29  /dev/tty36  /dev/tty43  /dev/tty50  /dev/tty58  /dev/tty8   /dev/ttyp3    /dev/ttypb  /dev/ttyS3


mwesi@mwesi-developer:~/vesc_ws$ ls
build  devel  src
mwesi@mwesi-developer:~/vesc_ws$ rostopic
bash: rostopic: command not found
mwesi@mwesi-developer:~/vesc_ws$ ls
build  devel  src
mwesi@mwesi-developer:~/vesc_ws$ source devel/setup.bash 
ROS_DISTRO was set to 'humble' before. Please make sure that the environment does not mix paths from different distributions.

mwesi@mwesi-developer:~/vesc_ws$ rostopic list
/commands/motor/brake
/commands/motor/current
/commands/motor/duty_cycle
/commands/motor/position
/commands/motor/speed
/commands/servo/position
/rosout
/rosout_agg
/sensors/core
/sensors/servo_position_command
mwesi@mwesi-developer:~/vesc_ws$ ros topic pub /commands/motor/speed std_msgs/msg/Float64 "data: 800.0"
bash: ros: command not found

mwesi@mwesi-developer:~/vesc_ws$ rostopic list
/commands/motor/brake
/commands/motor/current
/commands/motor/duty_cycle
/commands/motor/position
/commands/motor/speed
/commands/servo/position
/rosout
/rosout_agg
/sensors/core
/sensors/servo_position_command

mwesi@mwesi-developer:~/vesc_ws$ ros topic --help
bash: ros: command not found
mwesi@mwesi-developer:~/vesc_ws$ ros topic 
bash: ros: command not found
mwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/msg/Float64 "data: 800.0"
ERROR: invalid topic type: std_msgs/msg/Float64

mwesi@mwesi-developer:~/vesc_ws$ rostopic info /commands/motor/speed
Type: std_msgs/Float64

Publishers: None

Subscribers: 
 * /vesc_driver_node (http://mwesi-developer:42205/)


mwesi@mwesi-developer:~/vesc_ws$ rostopic info /commands/motor/speed /
/commands/motor/brake            /commands/motor/duty_cycle       /commands/motor/speed            /rosout                          /sensors/core
/commands/motor/current          /commands/motor/position         /commands/servo/position         /rosout_agg                      /sensors/servo_position_command


mwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/msg/Float64 "data: 800.0"
ERROR: invalid topic type: std_msgs/msg/Float64
mwesi@mwesi-developer:~/vesc_ws$ rostopic info /commands/motor/speed /
Usage: rostopic info /topic

rostopic: error: you may only specify one topic name
mwesi@mwesi-developer:~/vesc_ws$ rostopic info /commands/motor/speed 
Type: std_msgs/Float64

Publishers: None

Subscribers: 
 * /vesc_driver_node (http://mwesi-developer:42205/)


mwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/Float64 "data: 1000.0" 
publishing and latching message. Press ctrl-C to terminate
^C^C^Cmwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/Float64 "data: 2000.0" 
publishing and latching message. Press ctrl-C to terminate
^C^C^Cmwesi@mwesi-developer:~/vesc_ws$ 
mwesi@mwesi-developer:~/vesc_ws$ 
mwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/Float64 "data: 3000.0" 
publishing and latching message. Press ctrl-C to terminate
^C^C^C^C^C
mwesi@mwesi-developer:~/vesc_ws$ ^C
mwesi@mwesi-developer:~/vesc_ws$ ^C
mwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/Float64 "data: 5000.0" 
publishing and latching message. Press ctrl-C to terminate
^C^C^C^Cmwesi@mwesi-developer:~/vesc_ws$ rostopic pub /commands/motor/speed std_msgs/Float64 "data: 8000.0" 
publishing and latching message. Press ctrl-C to terminate
^C^C^C^Cmwesi@mwesi-developer:~/vesc_ws$ 
mwesi@mwesi-developer:~/vesc_ws$ 
mwesi@mwesi-developer:~/vesc_ws$ 
mwesi@mwesi-developer:~/vesc_ws$ ^C
mwesi@mwesi-developer:~/vesc_ws$ 

Unsafe (below, need to knock of a zero when testing on a bench)


rostopic pub -r 10 /commands/motor/speed std_msgs/Float64 "data: 30000.0"

To make the command continuous from the command line using `rostopic pub`, you need to specify the publishing rate to ensure that the command is sent repeatedly at a fixed interval. This will prevent the motor from stopping if it requires a continuous stream of commands to operate.

Here’s how you can modify your command to make it continuous:

```bash
rostopic pub -r 10 /commands/motor/speed std_msgs/Float64 "data: 30000.0"
```

In this command:
- The `-r 10` option sets the rate of publishing to 10 Hz, meaning the message will be published ten times per second. You can adjust this rate based on what your motor controller requires.
- `/commands/motor/speed` is the topic where the command is published.
- `std_msgs/Float64` is the type of the message being published.
- `"data: 30000.0"` specifies the content of the message, where `30000.0` is the speed value.

This command will continuously send the speed command at a rate of 10 Hz as long as the terminal is open and the command is running. This should help in maintaining the motor operation without interruptions. Adjust the rate as necessary for your specific setup.

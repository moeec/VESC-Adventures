"""
This script creates a ROS 2 node that publishes different speed values to the /commands/motor/speed topic according to the specified sequence. 
It uses a timer to change the speed after the specified duration for each speed setting.

The use of time.sleep() in a ROS node is generally not recommended because it can interfere with the normal operation of the node, especially in handling callbacks. However, for a simple script like this, it can be acceptable. For more complex applications, consider using ROS timers or another non-blocking approach.
This script will stop the motor and then shut down the node after completing the sequence. Adjust the script as necessary for your specific requirements.
Ensure that your ROS environment is properly configured, and the necessary dependencies are installed before running this script.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time

class MotorSpeedController(Node):
    def __init__(self):
        super().__init__('motor_speed_controller')
        self.speed_pub = self.create_publisher(Float64, '/commands/motor/speed', 10)
        self.create_timer(1.0, self.timer_callback)
        self.speeds = [13000.0, 15000.0, 25000.0, 0.0]
        self.durations = [2.0, 5.0, 10.0, 0]
        self.current_step = 0

    def timer_callback(self):
        if self.current_step < len(self.speeds):
            speed = Float64()
            speed.data = self.speeds[self.current_step]
            self.speed_pub.publish(speed)
            time.sleep(self.durations[self.current_step])
            self.current_step += 1
        else:
            self.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    motor_speed_controller = MotorSpeedController()

    try:
        rclpy.spin(motor_speed_controller)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()


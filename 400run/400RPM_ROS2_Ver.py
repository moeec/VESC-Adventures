import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time

class VescSpeedController(Node):
    def __init__(self):
        super().__init__('vesc_speed_controller')
        self.speed_pub = self.create_publisher(Float64, '/vesc/speed', 10)
        self.timer = self.create_timer(0.1, self.timer_callback) # 10 Hz
        self.end_time = self.get_clock().now() + rclpy.duration.Duration(seconds=10)
        self.speed = Float64()
        self.speed.data = 400
        self.running = True

    def timer_callback(self):
        if self.get_clock().now() < self.end_time and self.running:
            self.speed_pub.publish(self.speed)
        else:
            if self.running:
                # Stop the motor
                self.speed.data = 0
                self.speed_pub.publish(self.speed)
                self.running = False

def main(args=None):
    rclpy.init(args=args)
    vesc_speed_controller = VescSpeedController()

    try:
        rclpy.spin(vesc_speed_controller)
    except KeyboardInterrupt:
        pass
    finally:
        vesc_speed_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

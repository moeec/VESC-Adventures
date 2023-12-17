"""
This script will create a ROS 2 node that publishes motor speed commands following a sinusoidal profile. The amplitude and frequency of the sine wave can be adjusted by changing the self.amplitude and self.frequency variables, respectively.

Key Points:

 The timer_callback function is called at a frequency of 10 Hz.
 The elapsed_time is used to calculate the current value of the sinusoidal function.
 The motor speed is set based on the sinusoidal function, and the value is published to the /commands/motor/speed topic.
 When the script is interrupted (e.g., by a KeyboardInterrupt), it sends a final command to stop the motor.

Please ensure that the motor, VESC, and the system are set up safely before running this script, especially since sinusoidal control can lead to rapid changes in motor speed. Start with a lower amplitude and frequency to test and ensure everything functions as expected.

A separate thread (input_thread) is created to wait for the Enter key press.
The input_thread function waits for an Enter key press and then calls stop_motor on the controller object.
The stop_motor method in SinusoidalSpeedController sets the running flag to False and sends a command to stop the motor.
The main thread continues to run the ROS node and the sinusoidal speed control loop until the running flag is set to False.

With this setup, when you run the script, it will start the sinusoidal speed control, and you can press Enter at any time to stop the motor. The script will then exit gracefully.


The input_thread function sets sinusoidal_speed_controller.running to False when Enter is pressed. This stops the timer callback from publishing new speeds.
The stop_motor method now also destroys the timer to stop its callback from executing.
The main function has been modified to use rclpy.spin_once in a loop, which keeps running until sinusoidal_speed_controller.running is set to False. This approach allows for more controlled shutdown behavior.
The thread.daemon = True line ensures that the input thread will not prevent the program from exiting if the main thread completes its execution.
"""



import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import threading
import time

class SinusoidalSpeedController(Node):
    def __init__(self):
        super().__init__('sinusoidal_speed_controller')
        self.speed_pub = self.create_publisher(Float64, '/commands/motor/speed', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.start_time = self.get_clock().now()
        self.amplitude = 23000.0  # Max speed amplitude
        self.frequency = 0.5     # Frequency in Hz
        self.running = True

    def timer_callback(self):
        if self.running:
            elapsed_time = (self.get_clock().now() - self.start_time).nanoseconds / 1e9
            speed_value = self.amplitude * math.sin(2 * math.pi * self.frequency * elapsed_time)
            speed = Float64()
            speed.data = speed_value
            self.speed_pub.publish(speed)
        else:
            self.stop_motor()

    def stop_motor(self):
        stop_speed = Float64()
        stop_speed.data = 0.0
        self.speed_pub.publish(stop_speed)
        self.destroy_timer(self.timer)

def main(args=None):
    rclpy.init(args=args)
    sinusoidal_speed_controller = SinusoidalSpeedController()

    def input_thread(node):
        input("Press Enter to stop the motor and exit the program...")
        node.running = False

    # Start input thread
    thread = threading.Thread(target=input_thread, args=(sinusoidal_speed_controller,))
    thread.daemon = True
    thread.start()

    try:
        while rclpy.ok() and sinusoidal_speed_controller.running:
            rclpy.spin_once(sinusoidal_speed_controller, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        sinusoidal_speed_controller.stop_motor()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


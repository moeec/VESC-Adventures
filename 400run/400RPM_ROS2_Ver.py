the topics used by your VESC driver. Also, ensure that your VESC is properly configured and can handle the specified RPM.

"""

import rospy
from std_msgs.msg import Float64
import time

def run_vesc():
    # Initialize ROS node
    rospy.init_node('vesc_speed_controller', anonymous=True)

    # Create a publisher to send speed commands to VESC
    speed_pub = rospy.Publisher('/vesc/speed', Float64, queue_size=10)

    # Set the rate of publishing messages
    rate = rospy.Rate(10) # 10 Hz

    # Set speed in RPM
    speed = Float64()
    speed.data = 400

    # Run the motor at 400 RPM for 10 seconds
    end_time = rospy.Time.now() + rospy.Duration(10)
    while rospy.Time.now() < end_time:
        speed_pub.publish(speed)
        rate.sleep()

    # Stop the motor
    speed.data = 0
    speed_pub.publish(speed)

if __name__ == '__main__':
    try:
        run_vesc()
    except rospy.ROSInterruptException:
        pass

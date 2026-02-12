#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class GamepadReader(Node):
    def __init__(self):
        super().__init__('gamepad_reader')

        #subscribing to the gamepad output
        self.subscription = self.create_subscription(
            Joy, 'joy', self.joy_callback, 10)
        
        #publishing the robot commands
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info('Gamepad Reader Node has been started.')
    
    def joy_callback(self, msg):
        twist = Twist()
        #joystic logic
        forward_speed = msg.axes[1] * 1.0 #upper left joystick forward-backward motion scaled at 1m/s
        turning_speed = msg.axes[2] * 0.5 #lower right joystick left-right motion scaled at 0.5 rad/s
        
        twist.linear.x = float(forward_speed)
        twist.angular.z = float(turning_speed)

        #buttons logic
        if msg.buttons[7] == 1: #When R2 is pressed
            forward_speed*=1.10
        if msg.buttons[5] == 1: #When L2 is pressed
            forward_speed*=0.90  
        #stop buttton 3 (Circle button on PS4 controller) is pressed)
        if msg.buttons[2] == 1:
            self.get_logger().warn('STOP')
            forward_speed = 0.0
            turning_speed = 0.0
        self.publisher.publish(twist)
def main():
    rclpy.init()
    gamepad_node = GamepadReader()

    try:
        rclpy.spin(gamepad_node)

    except KeyboardInterrupt:
        pass
    gamepad_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':

    main()      
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class MyPublisherClass(Node):

    def __init__(self, topic, mymsg, name):
        super().__init__(name)
        self.mypub = self.create_publisher(type(mymsg), topic, 1)
        self.create_timer(0.1, self.mytimercallback)

    def mytimercallback(self, mymsg):
        self.mypub.publish(mymsg)

class MySubscriberClass(Node):

    def __init__(self, topic, mymsg, name):
        super().__init__(name)
        self.subscription = self.create_subscription(
            type(mymsg), topic, self.mysubcallback, 10)

    def mysubcallback(self, msg):
        print('You said: ', msg.data)

class GamepadReader(Node):
    def __init__(self):
        super().__init__('gamepad_reader')

        #subscribing to the gamepad output
        self.subscription = self.create_subscription(
            Joy, 'joy', self.joy_callback, 10)
        
        #publishing the robot commands
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        super().__init__('myfirstpublisher')
        self.mypub = self.create_publisher(String, 'myfirsttopic', 1)
        self.create_timer(0.1, self.mytimercallback)


#    def joy_callback(self, msg):
#        twist = Twist()
#
#        twist.linear.x = msg.axes[1] * 0.5 #scaling at max 0.5m/s
#        twist.angular.z  = msg. axes[0]*1.0 #scaling at 1 rad/s
#        self.publisher.publish(twist)
#        self.get_logger().info(f'Linear: {twist.linear.x}, Angular: {twist.angular.z}')

    def joy_callback(self, msg):
        #joystic logic
        forward_speed = msg.axes[1] #upper left joystick forward-backward motion
        turning_speeed = msg.axes[0] #lower right joystick left-right motion
        
        #buttons logic
        if msg.buttons[7] == 1: #When R2 is pressed
            forward_speed*=1.10
        if msg.buttons[5] == 1: #When L2 is pressed
            forward_speed/=1.10  
        #stop
        if msg.buttons[3] == 1:
            self.get_logger().warn('STOP')
            forward_speed = 0.0

def main():
    rclpy.init()
    gamepad_node = GamepadReader()

    try:
        rclpy.spin(gamepad_node)

    except KeyboardInterrupt:
        pass
    gamepad_node.destroy_node()
    rclpy.shutdown()
    #publishernode = MyPublisherClass()
    #try:
    #    rclpy.spin(publishernode)
    #except KeyboardInterrupt:
    #    pass
    #publishernode.destroy_node()
    #rclpy.shutdown()


if __name__ == '__main__':

    main()      
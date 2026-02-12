#!/usr/bin/env python3


import rclpy

from std_msgs.msg import String


def main():

    global mypub

    rclpy.init()

    publishernode = rclpy.create_node('myfirstpublisher')

    mypub = publishernode.create_publisher(String, 'myfirsttopic', 1)

    publishernode.create_timer(0.1, mytimercallback)

    try:

        rclpy.spin(publishernode)

    except KeyboardInterrupt:

        pass


    publishernode.destroy_node()

    rclpy.shutdown()


def mytimercallback():

    global mypub

    mymsg = String()

    mymsg.data = 'Hello ROS2 Communication'

    mypub.publish(mymsg)


if __name__ == '__main__':

    main()

    ##Alternative. Heere subscriber

    #!/usr/bin/env python3


import rclpy

from std_msgs.msg import String


def main():

    rclpy.init()

    subscribernode = rclpy.create_node('myfirstsubscriber')

    subscribernode.create_subscription(String, 'myfirsttopic', mysubcallback, 10)

    try:

        rclpy.spin(subscribernode)

    except KeyboardInterrupt:

        pass

    subscribernode.destroy_node()

    rclpy.shutdown()


def mysubcallback(msg):

    print('You said: ', msg.data)


if __name__ == '__main__':

    main
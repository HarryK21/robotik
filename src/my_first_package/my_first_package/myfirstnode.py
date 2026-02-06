#!/usr/bin/env python3
import rclpy

def main():
    rclpy.init()
    node = rclpy.create_node('firstnode')
    print("Node 'firstnode' gestartet. Drücke Strg+C zum Beenden.")
    try:
          rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
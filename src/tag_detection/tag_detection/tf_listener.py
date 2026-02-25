#!/usr/bin/env python3

import rclpy
import tf2_ros
from geometry_msgs.msg import TransformStamped

def printer(trans: TransformStamped):
    print("----------------------------------------")
    print("Position: ")
    print("  X: " + str(trans.transform.translation.x))
    print("  Y: " + str(trans.transform.translation.y))
    print("  Z: " + str(trans.transform.translation.z))
    print("Orientation: ")
    print("  X: " + str(trans.transform.rotation.x))
    print("  Y: " + str(trans.transform.rotation.y))
    print("  Z: " + str(trans.transform.rotation.z))
    print("  W: " + str(trans.transform.rotation.w))


def timercallback():
    global tfBuffer
    from_frame = "base_link"
    to_frame = "marker"
    
    try:
        # Use a small timeout (e.g., 100ms) to wait for the transform to become available
        now = rclpy.time.Time()
        trans = tfBuffer.lookup_transform(
            from_frame, 
            to_frame, 
            now, 
            timeout=rclpy.duration.Duration(seconds=0.1)
        )
        
        printer(trans)
        # REMOVED: tfBuffer.clear() - Keep the buffer intact!
        
    except tf2_ros.LookupException as e:
        print(f"Lookup failed: Transform not found ({e})")
    except tf2_ros.ConnectivityException as e:
        print(f"Lookup failed: Connectivity issue ({e})")
    except tf2_ros.ExtrapolationException as e:
        print(f"Lookup failed: Extrapolation error ({e})")
    except Exception as e:
        print(f"Unexpected error: {e}")
def main():
    global tfBuffer
    rclpy.init() # init ros client library
    nh = rclpy.create_node('tf2_listener') # create a node with name 'tf2_listener'
    tfBuffer = tf2_ros.Buffer(cache_time=rclpy.duration.Duration(nanoseconds=100000000)) # create a TF2 buffer which saves the TFs for given cache_time
    tf2_ros.TransformListener(tfBuffer, nh) # create TF2 listener which connects buffer with node
    nh.create_timer(0.25, timercallback) # call timercallback every 100ms
    try:
        rclpy.spin(nh) # spin node until exception
    except KeyboardInterrupt:
        nh.destroy_node() # destroy node
        rclpy.shutdown() # shutdown ros client library

if __name__ == '__main__':
    main()

    
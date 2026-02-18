from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # The standard ROS 2 Joy Node (reads the raw hardware)
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'dev': '/dev/input/js0', # Adjust if your controller is on a different port
                'deadzone': 0.05,
            }]
        ),
        
        # Your custom Gamepad Reader Node
        Node(
            package='teleop', # Replace with your actual package name
            executable='teleop_node', # Replace with the name in setup.py
            name='gamepad_reader',
            output='screen'
        )
    ])
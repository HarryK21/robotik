from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_proc',
            executable='rectify_node',
            name='rectify_node',
            # This is where your --remap goes
            remappings=[
                ('image', 'image_raw'),
            ],
            # Optional: if you want to see the output in the console
            output='screen'
        )
    ])
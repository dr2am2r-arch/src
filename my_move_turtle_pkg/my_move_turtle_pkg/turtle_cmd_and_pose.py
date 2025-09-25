import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from my_first_package_msgs.msg import CmdAndPoseVel

class CmdAndPose(Node):
    def __init__(self):
        super().__init__('turtle_cmd_pose')
        self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
        self.cmd_pose = CmdAndPoseVel()

    def callback_pose(self, msg):
        self.cmd_pose.pose.x = msg.x
        self.cmd_pose.pose.y = msg.y
        self.cmd_pose.linear_vel = msg.linear_velocity
        self.cmd_pose.angular_vel = msg.angular_velocity
        print(self.cmd_pose)

def main(args=None):
    rclpy.init(args=args)
    node = CmdAndPose()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

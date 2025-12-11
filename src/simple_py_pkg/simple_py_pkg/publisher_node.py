import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChannelPublisher(Node):
    def __init__(self):
        super().__init__('channel_publisher')
        self.publisher_ = self.create_publisher(String, '/channel_something', 10)
        timer_period = 1.0  # 1 saniyede bir mesaj yayınla
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0
        self.get_logger().info('Publisher başlatıldı: /channel_something')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello from ROS2! Sayı: {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Gönderilen mesaj: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = ChannelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

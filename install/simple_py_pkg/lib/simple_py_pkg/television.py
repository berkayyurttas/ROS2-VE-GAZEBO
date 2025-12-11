#!/usr/bin/env python3

# 1. Library
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String  # <-- doğru paket ismi

# 2. Node Sınıfı
class ChannelNode(Node):
    def __init__(self):
        super().__init__("channel_node")

        self.greeting_= "Hi awesome people :)"
        self.publisher_ = self.create_publisher(String, "channel_something", 10)  # topic adı + queue size
        self.timer_ = self.create_timer(0.5, self.publish_channel)
        self.get_logger().info("Channel Something has been published !")


    def publish_channel(self):
        msg = String()
        msg.data = str(self.greeting_) + "\nWelcome to the Channel Something"
        self.publisher_.publish(msg)


# 3. main fonksiyonu
def main(args=None):
    rclpy.init(args=args)
    node = ChannelNode()
    rclpy.spin(node)
    rclpy.shutdown()

# 4. main block
if __name__ == "__main__":
    main()

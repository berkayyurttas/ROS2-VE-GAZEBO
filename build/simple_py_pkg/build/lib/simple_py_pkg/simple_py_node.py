#!/usr/bin/env python3

# 1. Library
import rclpy
from rclpy.node import Node


# 2. Metod
def main(args=None):
    rclpy.init(args=args)
    node = Node("py_node")
#print("Hello world!")
    node.get_logger().info("Hello World!")

    rclpy.spin(node)
    rclpy.shutdown()


    

# 3. "if _name_"block

if __name__ == "__main__": 

    main()

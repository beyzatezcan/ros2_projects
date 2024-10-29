import rclpy #ros2 kutuphanesi
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
            super().__init__("python_test")
            self.counter_ = 0 
            self.get_logger().info("hello ros2")
            self.create_timer(0.5,self.timer_callback)
    def timer_callback(self):
            self.counter_+=1
            self.get_logger().info(f"welcome{self.counter_}")
            

def main(args=None):
    rclpy.init(args = args)
    node=MyNode()
    rclpy.spin(node) #bitmemesi icin spine alinir ve ctrl+c ile cikilir
    rclpy.shutdown() #bitirir
if __name__== "__main__" :
    main()
 #colcon build ederken colcon build --packages-select dosyaadi yaparsak tek dosyayi build ederiz
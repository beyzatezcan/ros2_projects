import rclpy #ros2 kutuphanesi
from rclpy.node import Node
def main(args=None):
    rclpy.init(args=args)
    node=Node("python_test")
    node.get_logger().info("hello ros2")
    rclpy.spin(node) #bitmemesi icin spine alinir ve ctrl+c ile cikilir
    rclpy.shutdown() #bitirir
if __name__=="__main__" :
 main()
 #colcon build ederken colcon build --packages-select dosyaadi yaparsak tek dosyayi build ederiz
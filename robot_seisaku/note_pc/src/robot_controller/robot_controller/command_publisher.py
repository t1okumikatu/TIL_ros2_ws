import rclpy
from rclpy.node import Node
#from std_msgs.msg import String
from geometry_msgs.msg import Twist
class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.01  #seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.vel = Twist() #変数velをTwist型に
        self.vel.linear.x = 0.0 #初期化
        self.vel.angular.z = 0.0
    def timer_callback(self):
        key = input('f, b, r, l, s >> Enter <<')
        if key == 'f': #forward
            self.vel.linear.x += 0.1 #並進xを直進速度とする
        elif key == 'b': #back
            self.vel.linear.x -= 0.1
        elif key == 'l': #left
            self.vel.angular.z += 0.1 #回転zを旋回速度とする
        elif key == 'r': #right
            self.vel.angular.z -= 0.1
        elif key == 's': #stop
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
        else:
            pass
        self.publisher_.publish(self.vel)
        self.get_logger().info(f'並進速度={self.vel.linear.x}角速度={self.vel.angular.z}')
def main(args=None):
    rclpy.init(args=args)
    command_publisher = CommandPublisher()
    rclpy.spin(command_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically   # when the garbage collector destroys the node object) 
    command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


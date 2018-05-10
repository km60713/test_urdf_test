#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from time import sleep

def move():
    # Starts a new node
    rospy.init_node('straightpy', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    r = rospy.Rate(10) # 10hz
    vel_msg = Twist()

    #input speed
    speed = int(input("input speed(m/s) e.g. 5 : "))
    rotate = int(input('input rotate speed(rad/s) e.g. 0.1 : '))
    distance = int(input('input the distance(m) you want to run e.g. 80 : '))
    
    # Movement information
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = rotate

    #Wait fo few seconds
    sleep(3)
    current_distance = 0
    t0 = rospy.Time.now().to_sec()
    
    while not rospy.is_shutdown():
        #Loop to move
        if(current_distance < distance):
            t1 = rospy.Time.now().to_sec()
            dift = t1 - t0
            current_distance += speed * dift
            t0 = t1
        else:
            vel_msg.linear.x = 0

        velocity_publisher.publish(vel_msg)
        r.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass

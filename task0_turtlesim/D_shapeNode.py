#!/usr/bin/env python3

import sys
import traceback
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

theta = 0

currentpos = Pose()

def callback_pose(msg):
    global theta    
    global currentpos
    
    currentpos = msg
    print(msg.theta)
    theta = msg.theta

def main():
    global theta
    rospy.init_node('task_0',  anonymous= True)
    pub = rospy.Publisher('/turtle1/cmd_vel',  Twist,  queue_size=10)
    vel = Twist()
    loop_rate = rospy.Rate(50)
    
    
    rospy.Subscriber("/turtle1/pose", Pose, callback_pose)
    
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
    pub.publish(vel)
    
    
    while  theta >= 0:
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1
        
        rospy.loginfo("Publishing Linear Velocity: %.2f and Angular Velocity: %.2f", vel.linear.x, vel.angular.z)
        pub.publish(vel)
        loop_rate.sleep()
        
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
    pub.publish(vel)
    
    
    while  theta <= -1.5708:          
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1
        
        rospy.loginfo("Publishing Linear Velocity: %.2f and Angular Velocity: %.2f", vel.linear.x, vel.angular.z)
        pub.publish(vel)
        loop_rate.sleep()
        
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
    pub.publish(vel)
    
    while currentpos.y >= 5.5444:          
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        
        rospy.loginfo("Publishing Linear Velocity: %.2f and Angular Velocity: %.2f", vel.linear.x, vel.angular.z)
        pub.publish(vel)
        loop_rate.sleep()
        
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
    pub.publish(vel)
    

if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        main()

    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")

#!/usr/bin/env python3

import rospy

# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Twist
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry

# for finding sin() cos() 
import math

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from tf.transformations import euler_from_quaternion


hola_x = 0
hola_y = 0
hola_theta = 0

def odometryCb(msg):
	global hola_x, hola_y, hola_theta
	hola_x = msg.pose.pose.position.x
	hola_y = msg.pose.pose.position.y
	_, _, hola_theta = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])


def main():
	# Initialze Node
	rospy.init_node('controller',  anonymous= True)
	# We'll leave this for you to figure out the syntax for 
	# initialising node named "controller"
	
	# Initialze Publisher and Subscriber
	rospy.Subscriber("/odom", Odometry, odometryCb)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	# We'll leave this for you to figure out the syntax for
	# initialising publisher and subscriber of cmd_vel and odom respectively

	# Declare a Twist message
	vel = Twist()

	# Initialise the required variables to 0

	#Tolerances

	#desired pose
	x_d = 0
	y_d = 0
	theta_d = 0
	
	# desired pose Array index position
	i = 0

	#Error in global frame
	e_x_g = 0
	e_y_g = 0
	e_theta_gl = 0

	# Error in local frame
	e_x_l = 0
	e_y_l = 0

	#Variables for PID controller
	vel_x = 0
	vel_y = 0
	vel_z = 0
	
	# Need to find these values by tuning and trial-error.
	kp_x = 0
	kp_y = 0
	kp_theta = 0
	
	
	# <This is explained below>
	
	# For maintaining control loop rate.
	rate = rospy.Rate(100)

	# Initialise variables that may be needed for the control loop
	# For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
	# and also Kp values for the P Controller

	#control loop
	
	while not rospy.is_shutdown():

		# 
		# Find error (in x, y and theta) in global frame
		# the /odom topic is giving pose of the robot in global frame
		# the desired pose is declared above and defined by you in global frame
		# therefore calculate error in global frame
		e_x_g = x_d - hola_x
		e_y_g = y_d - hola_y
		e_theta_gl = theta_d - hola_theta

		if((abs(e_x_g) <= 0.05) and (abs(e_y_g) <= 0.05) and (abs(e_theta_gl) <= 0.0174533)):
			break
		

 
		# (Calculate error in body frame)
		# But for Controller outputs robot velocity in robot_body frame, 
		# i.e. velocity are define is in x, y of the robot frame, 
		# Notice: the direction of z axis says the same in global and body frame
		# therefore the errors will have have to be calculated in body frame.
		e_x_l = e_x_g*math.cos(hola_theta) - e_y_g*math.sin(hola_theta)
		e_y_l = e_x_g*math.sin(hola_theta) + e_y_g*math.cos(hola_theta)


		
		# This is probably the crux of Task 1, figure this out and rest should be fine.
	
		# Finally implement a P controller 
		# to react to the error with velocities in x, y and theta.
		vel_x = kp_x*e_x_l
		vel_y = kp_y*e_y_l
		vel_z = kp_theta*e_theta_gl


		# Safety Check
		# make sure the velocities are within a range.
		# for now since we are in a simulator and we are not dealing with actual physical limits on the system 
		# we may get away with skipping this step. But it will be very necessary in the long run.

		vel.linear.x = vel_x
		vel.linear.y = vel_y
		vel.angular.z = vel_z
		pub.publish(vel)
		rate.sleep()
		
	vel.linear.x = 0
	vel.linear.y = 0
	vel.angular.z = 0
	pub.publish(vel)
	rate.sleep()
		


if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass

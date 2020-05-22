#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def orientate0 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	if (xgoal-x < 0 and ygoal-y == 0):
		desired_angle_goal = (math.pi/2)+math.pi
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = 0.0
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (dtheta < 0.01):
            break

def go_to_goal0 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 0.5				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	if (xgoal-x < 0 and ygoal-y == 0):
		desired_angle_goal = math.pi
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (distance < 0.01):
            break



def orientate1 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = 0.0
        velocity_message.angular.z = abs(angular_speed)
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (dtheta < 0.01):
            break

def go_to_goal1 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 0.5				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = abs(angular_speed)
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (distance < 0.01):
            break





def orientate2 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
        
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = 0.0
        velocity_message.angular.z = -abs(angular_speed)
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (dtheta < 0.01):
            break

def go_to_goal2 (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 2.0				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 16.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = (-math.pi/2)-0.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+0.01
	else:
		desired_angle_goal = math.atan2(ygoal-y,xgoal-x)
	dtheta = desired_angle_goal-theta        
	angular_speed = ka * (dtheta)

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = -abs(angular_speed)
        velocity_publisher.publish(velocity_message)
        print ('x=', x, 'y=', y)

        if (distance < 0.01):
            break



if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)     

	
	global x
	global y
	rotacion=0
	xinicial=5.5
	yinicial=6
	orientate0(xinicial,yinicial)
	go_to_goal0(xinicial,yinicial)

	if(rotacion==1):
		xinicial=10
		yinicial=1

		orientate0(xinicial,yinicial)
		go_to_goal0(xinicial,yinicial)
		
		
		xAux = x
		yAux = y + 9
		orientate0(xAux,yAux)
		time.sleep(0.1)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)

		xAux = xAux - 9
		yAux = yAux 
		orientate0(xAux,yAux)
		time.sleep(0.1)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)
		

		xAux = xAux
		yAux = yAux - 9
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)

		xAux = xAux + 9
		yAux = yAux
		orientate0(xAux,yAux)
		time.sleep(0.1)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)
		
	if(rotacion==0):

		xinicial=1
		yinicial=10
		orientate0(xinicial,yinicial)
		go_to_goal0(xinicial,yinicial)
		
		

		xAux = x + 9
		yAux = y
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		orientate0(xAux,yAux)
		time.sleep(1.0)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)
		

		


		
		xAux = 10
		yAux = y -9
		orientate0(xAux,yAux)
		time.sleep(1.0)
		go_to_goal0(xAux,yAux)
		time.sleep(0.1)



		xAux = x - 9
		yAux = y 
		orientate1(xAux,yAux)
		time.sleep(0.1)
		go_to_goal1(xAux,yAux)
		time.sleep(0.1)

		
		xAux = xAux
		yAux = yAux + 9
		orientate1(xAux,yAux)
		time.sleep(0.1)
		go_to_goal1(xAux,yAux)
		time.sleep(0.1)
		
	

	time.sleep(1.0)		


    except rospy.ROSInterruptException:        
	pass

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

def orientate (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        ka = 4.0
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = -(math.pi/2)-.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+.01
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

def go_to_goal (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    cmd_vel_topic = '/turtle1/cmd_vel'

    while(True):
        kv = 0.5			
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 4
	if (xgoal-x == 0 and ygoal-y < 0):
       		desired_angle_goal = -(math.pi/2)-.01
        if (xgoal-x == 0 and ygoal-y > 0):
		desired_angle_goal = (math.pi/2)+.01
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

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)     
	r=4.5
	xi=5.5
	yi=5.5
	giro=0
	

	if(giro==1):
		for i in range(0,361,10):
			if((i>=0 and i<90)):
					
				xn = xi+r*math.cos((i*math.pi)/180)
				yn = yi+r*math.sin((i*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>90 and i<=180):
				xn = xi-r*math.sin(((i-90)*math.pi)/180)
				yn = yi+r*math.cos(((i-90)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>=180 and i<=270):
				xn = xi-r*math.cos(((i-180)*math.pi)/180)
				yn = yi-r*math.sin(((i-180)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>=270 and i<361):
				xn = xi+r*math.sin(((i-270)*math.pi)/180)
				yn = yi-r*math.cos(((i-270)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
	



	
	if(giro==0):
		for i in range(0,361,10):
			if(i>=0 and i<90):
					
				xn = xi+r*math.cos(((-i)*math.pi)/180)
				yn = yi+r*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>=90 and i<180):
					
				
				xn = xi+r*math.cos(((i)*math.pi)/180)
				yn = yi-r*math.sin(((i)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>=180 and i<270):
				xn = xi+r*math.cos(((-i)*math.pi)/180)
				yn = yi+r*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)
			if(i>=270 and i<361):
				xn = xi+r*math.cos(((-i)*math.pi)/180)
				yn = yi+r*math.sin(((-i)*math.pi)/180)
				orientate(xn,yn)
				go_to_goal(xn,yn)

		

				

    except rospy.ROSInterruptException:        
	pass

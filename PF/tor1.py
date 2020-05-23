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

def poseCallback1(pose_message):
    global x
    global y
    global theta
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta

def poseCallback2(pose_message):
    global x2
    global y2
    global theta2
    
    x2 = pose_message.x
    y2 = pose_message.y
    theta2 = pose_message.theta
    #print ('x2=', x2, 'y2=', y2)

def poseCallback3(pose_message):
    global x3
    global y3
    global theta3
    
    x3 = pose_message.x
    y3 = pose_message.y
    theta3 = pose_message.theta
    #print ('x3=', x3, 'y3=', y3)


def poseCallback4(pose_message):
    global x4
    global y4
    global theta4
    
    x4 = pose_message.x
    y4 = pose_message.y
    theta4 = pose_message.theta

def poseCallback5(pose_message):
    global x5
    global y5
    global theta5
    
    x5 = pose_message.x
    y5 = pose_message.y
    theta5 = pose_message.theta
    #print ('x2=', x2, 'y2=', y2)

def poseCallback6(pose_message):
    global x6
    global y6
    global theta6
    
    x6 = pose_message.x
    y6 = pose_message.y
    theta6 = pose_message.theta
    #print ('x3=', x3, 'y3=', y3)

def midpoint ():
    global pm
    global xm
    global ym
    d2 = abs(math.sqrt(((x2-x)**2)+((y2-y)**2)))
    d3 = abs(math.sqrt(((x3-x)**2)+((y3-y)**2)))
    d4 = abs(math.sqrt(((x4-x)**2)+((y4-y)**2)))
    d5 = abs(math.sqrt(((x5-x)**2)+((y5-y)**2)))
    d6 = abs(math.sqrt(((x6-x)**2)+((y6-y)**2)))
    print ('x2=', x2, 'y2=', y2)     
    print ('x3=', x3, 'y3=', y3)

    if(d2<1):
    	if(d3<1):
    		xm = (x2+x3)
    		ym = (y2+y3)
    		pm = True
    	elif(d4<1):
    		xm = (x2+x4)
    		ym = (y2+y4)
    		pm = True
    	elif(d5<1):
    		xm = (x2+x5)
    		ym = (y2+y5)
    		pm = True
    	elif(d6<1):
    		xm = (x2+x6)
    		ym = (y2+y6)
    		pm = True
    elif(d3<1):
    	if(d4<1):
    		xm = (x3+x4)
    		ym = (y3+y4)
    		pm = True
    	elif(d5<1):
    		xm = (x3+x5)
    		ym = (y3+y5)
    		pm = True
    	elif(d6<1):
    		xm = (x3+x6)
    		ym = (y3+y6)
    		pm = True
    elif(d4<1):
    	elif(d5<1):
    		xm = (x4+x5)
    		ym = (y4+y5)
    		pm = True
    	elif(d6<1):
    		xm = (x4+x6)
    		ym = (y4+y6)
    		pm = True	
    elif(d5<1):
    	elif(d6<1):
    		xm = (x5+x6)
    		ym = (y5+y6)
    		pm = True
    else:
    	pm = False	
    	
    

    print ('xm=', xm, 'ym=', ym)        

def orientate (xg, yg):
    
	global x
	global y
	global theta
    global ym
    global xm
    global pm

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

	xgoal=xg
    ygoal=yg
	while(True):
	xgoal=xg
    ygoal=yg
	  	midpoint ():
    	if(pm):
    		xgoal=xm
    		ygoal=ym
		ka = 1.0
		desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
		
		if desired_angle_goal < 0:
			desired_angle_goal = desired_angle_goal + 2*math.pi
			dtheta = desired_angle_goal - theta
			#print ('theta=', theta)			
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal
			dtheta = desired_angle_goal - theta	
			#print ('new_angle=', desired_angle_goal)

		#if abs(desired_angle_goal - theta) < abs((desired_angle_goal + 2*math.pi) - theta):	
		#	dtheta = desired_angle_goal - theta
		#	print ('dtheta=', dtheta)
		#else:
		#	dtheta = desired_angle_goal + 2*math.pi - theta
		#	print ('dtheta=', dtheta)        
		#
		if (abs(dtheta) < 0.005):
			print ('angle', theta*360.00/6.2831, 'reached')
			time.sleep(1)
			break

		angular_speed = ka * dtheta

		velocity_message.linear.x = 0.0
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)
      
def go_to_goal (xg, yg):
	    	
	global x
	global y
	global theta
    global ym
    global xm
    global pm

	velocity_message = Twist()
	cmd_vel_topic = '/turtle1/cmd_vel'

    xgoal=xg
    ygoal=yg
	while(True):
	xgoal=xg
    ygoal=yg
	  	midpoint ():
    	if(pm):
    		xgoal=xm
    		ygoal=ym
		ka = 5.0
		desired_angle_goal = math.atan2(ygoal+0.01-y, xgoal+0.01-x)
		#print ('desired_angle=', desired_angle_goal)

		if (desired_angle_goal < 0.0):	
			desired_angle_goal = desired_angle_goal + 6.2831
			#print ('new_angle=', desired_angle_goal)
		else:
			desired_angle_goal = desired_angle_goal	
			#print ('new_angle=', desired_angle_goal)

		dtheta = desired_angle_goal-theta
		#print ('dtheta=', dtheta)        
		angular_speed = ka * (dtheta)	
		

		if (abs(angular_speed) < 0.5):	
			angular_speed = angular_speed
		else:
			angular_speed = 0.0

		kv = 1.0				
		distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
		linear_speed = kv * distance

		if (distance < 0.1):
		    print ('point (', x, ',',  y, ') reached')
		    time.sleep(1)
		    break        

		velocity_message.linear.x = linear_speed
		velocity_message.angular.z = angular_speed
		velocity_publisher.publish(velocity_message)
		#print ('x=', x, 'y=', y)
       
if __name__ == '__main__':
	try:

		rospy.init_node('turtlesim_motion_pose', anonymous = True)

		cmd_vel_topic = '/turtle1/cmd_vel'
		velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

		position_topic1 = "/turtle1/pose"
        pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback1)

        position_topic2 = "/turtle2/pose"
        pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback2)

        position_topic3 = "/turtle3/pose"
        pose_subscriber3 = rospy.Subscriber(position_topic3, Pose, poseCallback3)

        position_topic4 = "/turtle4/pose"
        pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback4)

        position_topic5 = "/turtle5/pose"
        pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback5)

        position_topic6 = "/turtle6/pose"
        pose_subscriber3 = rospy.Subscriber(position_topic3, Pose, poseCallback6)
        
        time.sleep(2.0)	
		xgo=5
		ygo=10

        time.sleep(2.0)     

        orientate(xgo,ygo)
        time.sleep(0.5)
        go_to_goal(xgo,ygo)
        time.sleep(0.5) 

		

	except rospy.ROSInterruptException:        
		pass

#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from exercise_three.msg import UserInfo

publisher = rospy.Publisher('user_info', UserInfo, queue_size = 20)

def callback(message):
	user = UserInfo()
	data = message.data.split(',')
	user.name = data[0].split()[1]
	user.age = int(data[1].split()[1])
	user.height = int(data[2].split()[1])
	publisher.publish(user)

def program():
	rospy.init_node('data_processing')
	rospy.Subscriber('raw_data', String, callback)	
	rospy.spin()
	
if __name__ == '__main__':
	program()

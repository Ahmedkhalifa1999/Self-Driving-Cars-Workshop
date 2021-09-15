#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(message):
	data = message.data.split(',')
	name = data[0].split()[1]
	age = int(data[1].split()[1])
	height = int(data[2].split()[1])
	rospy.loginfo("name: %s\nage: %d\nheight: %d\n", name, age, height)

def program():
	rospy.init_node('data_processing')
	rospy.Subscriber('raw_data', String, callback)
	rospy.spin()
	
if __name__ == '__main__':
	program()

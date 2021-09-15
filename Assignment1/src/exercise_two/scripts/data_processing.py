#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int64

namePublisher = rospy.Publisher('name', String, queue_size = 20)
agePublisher = rospy.Publisher('age', Int64, queue_size = 20)
heightPublisher = rospy.Publisher('height', Int64, queue_size = 20)

def callback(message):
	data = message.data.split(',')
	name = data[0].split()[1]
	age = int(data[1].split()[1])
	height = int(data[2].split()[1])
	namePublisher.publish(name)
	agePublisher.publish(age)
	heightPublisher.publish(height)

def program():
	rospy.init_node('data_processing')
	rospy.Subscriber('raw_data', String, callback)	
	rospy.spin()
	
if __name__ == '__main__':
	program()

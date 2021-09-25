#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def program():
	name = input("name: ")
	age = input("age: ")
	height = input("height: ")
	publisher = rospy.Publisher('raw_data', String, queue_size = 20)
	rospy.init_node('user_info_driver')
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		publisher.publish('name: ' + name + ', age: ' + age + ', height: ' + height)
		rate.sleep()
		
		
if __name__ == '__main__':
	try:
		program()
	except rospy.ROSInterruptException:
		pass

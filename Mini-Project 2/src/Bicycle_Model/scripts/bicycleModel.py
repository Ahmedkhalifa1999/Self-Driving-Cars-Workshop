import rospy
from std_msgs import Float64MultiArray
import math

timestep = 0.01
length = 1.5
state = [0, 0, 0]
pub = rospy.Publisher('state', Float64MultiArray, queue_size = 10)

def propagate(message):
    state[0] += message[0] * math.cos(state[2]) * timestep
    state[1] += message[0] * math.cos(state[2]) * timestep
    state[2] += ((message[0] * math.tan(message[1])) / length) * timestep
    pub.publish(state)
    

def model():
    rospy.init_node('bicycleModel')
    rospy.Subscriber('SpeedandDirection', Float64MultiArray, callback=propagate)
    rospy.spin()

if __name__ == '__main__':
    model()

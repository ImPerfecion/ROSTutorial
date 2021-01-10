#!/usr/bin/python3

import rospy

if __name__ =='__main__':
    rospy.init_node('my_first_python_node')

    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10)

    #As long as the node is not shutdown, continue the programm
    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        #keeps the programm running with every 0.010seconds
        rate.sleep()


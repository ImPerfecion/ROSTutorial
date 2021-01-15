#!/usr/bin/python3


import rospy
from std_msgs.msg import Int64


if __name__ == '__main__':
    rospy.init_node('number_publisher', anonymous=True)

#Topic Name, Datentyp, Buffer
    pub = rospy.Publisher("/number",Int64, queue_size=10)

    #Publish with 2 Hertz
    rate = rospy.Rate(0.25)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = 1
        pub.publish(msg)
        rate.sleep()


    rospy.loginfo("Node was stopped")
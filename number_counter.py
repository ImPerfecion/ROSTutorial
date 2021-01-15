#!/usr/bin/python3


import rospy
from std_msgs.msg import Int64

New_number = 0
pub = None


def callback_receive_number_data(msg):
    global New_number
    New_number = New_number + msg.data
    Pub_number = Int64()
    Pub_number.data = New_number
    pub.publish(Pub_number)




if __name__== '__main__':
    rospy.init_node('number_counter')
    
    sub = rospy.Subscriber("/number",Int64,callback_receive_number_data)

    pub = rospy.Publisher("/number_count",Int64, queue_size=10)
    #So eine art loop funktion, die die obrigen Zeilen immer wieder aufruft
    rospy.spin()


    
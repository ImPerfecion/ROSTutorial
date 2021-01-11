#!/usr/bin/python3


import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node('robot_news_radio_transmitter')

#Topic Name, Datentyp, Buffer
    pub = rospy.Publisher("/robot_news_radio",String, queue_size=10)

    #Publish with 2 Hertz
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = 'Hi, jetzt sende ich meine Topics in die Welt hinaus'
        pub.publish(msg)
        rate.sleep()


    rospy.loginfo("Node was stopped")
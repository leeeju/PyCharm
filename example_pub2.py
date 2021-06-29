#!/usr/bin/env python

import rospy                   
from std_msgs.msg import String 

def get_hello(msg):               
    
    rospy.init_info(rospy.get_caller_id() + 'messge : %s' , msg.data)
 

if __name__ == '__main__':  
     rospy.init_node('sample_sub')
     rospy.Subscriber('hello',String, get_hello)
  
     rospy.spin()
     

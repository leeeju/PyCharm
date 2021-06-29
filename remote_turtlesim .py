#!/usr/bin/env python

import rospy
from GetChar import GetChar   
from geometry_msgs.msg import Twist
                          

if __name__ == '__main__':

   rospy.init_node("move_turtlesim")
    pb = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
  
    tw  = Twist()
    key = GetChar()
   
    tw.linear.x = 0.5
    tw.angular.z = 0.5
    
    ch = "~"

    while ch != 'Q':
        
       ch = key.getch()
       
       if ch == 'w' :
           tw.linear.x = 2.0; tw.angular.z = 2.0;   print "forward"
           
       elif ch == 's' :
           tw.linear.x = -2.0; tw.angular.z = 2.0;   print "backward"
           
       elif ch == 'a' :
           tw.angular.z = 2.0; tw.linear.x = 2.0;  print "rotate ccw"
           
       elif ch == 'd' :
           tw.angular.z = -2.0; tw.linear.x = 2.0;  print "rotate cw "  
            
       else: pass  
           
            
       
	   pb.publish(tw)
	   

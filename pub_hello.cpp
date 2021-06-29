#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>
int main(int argc, char **argv) {
  ros::init(argc, argv, "pub_hello");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<std_msgs::String>("/hello", 10);

  ros::Rate loop_rate(10);
  int count = 0;
  
  while (ros::ok()) {
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello~ " << count;
    msg.data = ss.str();

    //ROS_INFO("%s", msg.data.c_str());
    
    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }
  return 0;
}

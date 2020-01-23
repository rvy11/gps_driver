#!/usr/bin/env python
import rospy
import utm
from std_msgs.msg import Float64
import random

if __name__ == "__main__":
	try:
		rospy.init_node("gps_driver")
		out = rospy.Publisher("/gps_out_meters", Float64, queue_size=10)
		random.seed()
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			reading = random.random()
			rospy.loginfo("m = %.2f" % (reading))
			out.publish(reading)
			rate.sleep()
	except rospy.ROSInterruptException:
		pass

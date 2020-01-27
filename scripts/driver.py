#!/usr/bin/env python
import rospy
import utm
from std_msgs.msg import Float64
from gps_driver.msg import GNSS
import random

if __name__ == "__main__":
	try:
		rospy.init_node("gps_driver")
		out = rospy.Publisher("/gps_out", GNSS, queue_size=10)
		random.seed()
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			msg = GNSS()
			reading = random.random()
			rospy.loginfo("m = %.2f" % (reading))
			out.publish(msg)
			rate.sleep()
	except rospy.ROSInterruptException:
		pass

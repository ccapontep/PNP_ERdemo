#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: personhere_condition.py
# Author: Cecilia Aponte
'''

import rospy
from sensor_msgs.msg import LaserScan

def persondist_cb(msg):

    # middle position in the range is the position right in front of the robot
    cp = len(msg.ranges)/2  # central point
    # min value of 20 central points
    laser_center_dist = min(msg.ranges[cp-10:cp+10])
    # print 'distance to obstacle', laser_center_dist

    conditionName = "personhere"
    param = "PNPconditionsBuffer/" + conditionName
    if laser_center_dist < 1.1:
        # print 'Obstacle right in front'
        rospy.set_param(param, 1)
    else:
        rospy.set_param(param, 0)
        # print 'No obstacle'



# if __name__ == "__main__":
rospy.init_node('personhere_cond')
laser_sub = rospy.Subscriber("/scan", LaserScan, persondist_cb)
rospy.spin()

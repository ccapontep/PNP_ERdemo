#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: closeddoor_condition.py
# Author: Cecilia Aponte
'''

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion

map_robot_pose = None

def localizer_cb(data):
    # get current robot position
    global map_robot_pose

    if (map_robot_pose is None):
        map_robot_pose = [0,0,0]

    map_robot_pose[0] = data.pose.pose.position.x
    map_robot_pose[1] = data.pose.pose.position.y
    o = data.pose.pose.orientation
    q = (o.x, o.y, o.z, o.w)
    euler = euler_from_quaternion(q)
    map_robot_pose[2] = euler[2] # yaw
    print 'x:', map_robot_pose[0],'y:', map_robot_pose[1]
    print 'angle of robot is', euler[2], '\n'
    # consulting room corridor coordinates
    # CR_x1 = 35.33
    # CR_x2 = 58.37
    # CR_y1 = 24.32
    # CR_y2 = 28.11
    # (x > CR_x1 and x < CR_x2 and y > CR_y1 and y < CR_y2)



def doorclosed_cb(msg):

    if (map_robot_pose is None):
        return

    x = map_robot_pose[0]
    y = map_robot_pose[1]
    angle = map_robot_pose[2]

    # coordinates of locations outside of each consulting room
    CR_y = [24.65, 25.65] #25.15
    CR1_x = [37.7, 38.7] #38.2
    CR2_x = [43.34, 44.34] #43.84
    CR3_x = [49.4, 50.4] #49.9
    CR4_x = [54.94, 55.94] #55.44

    conditionName = "doorclosed"
    param = "PNPconditionsBuffer/" + conditionName

    # print 'x:', x, '\ty:', y
    # print getRobotPose('',0,0,0)
    # print getRobotPose()

    # check if robot is inside the corridor
    if (CR_y[0] <= y <= CR_y[1]) and (CR1_x[0] <= x <= CR1_x[1] or CR2_x[0] <= x <= CR2_x[1] or CR3_x[0] <= x <= CR3_x[1] or CR4_x[0] <= x <= CR4_x[1]):
        print 'In location outside of door'
        if angle <= 0.035 and angle > -0.035:
            # middle position in the range is the position right in front of the robot
            pp = 719
            laser_center_dist = min(msg.ranges[pp-10:pp+10])

        elif angle >= 3.1 and angle <= 3.14:
            pp = 0
            laser_center_dist = min(msg.ranges[pp-10:pp+10])
        else: laser_center_dist = 0

        if laser_center_dist > 1.6:
            print 'Door open'
            rospy.set_param(param, 0)
        else:
            print 'Door closed'
            rospy.set_param(param, 1)
    else:
        rospy.set_param(param, 0)


rospy.init_node('closeddoor_cond')
localizer_sub = rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped, localizer_cb)
odom_sub = rospy.Subscriber('/scan', LaserScan, doorclosed_cb)

rospy.spin()

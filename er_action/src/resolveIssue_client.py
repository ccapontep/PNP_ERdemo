#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: resolveIssue_client.py
# Author: Cecilia Aponte
'''

import rospy
import actionlib
from er_action_msgs.msg import ResolveIssueAction, ResolveIssueGoal, ResolveIssueResult, ResolveIssueFeedback



def ResolveIssue_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('resolveIssue_as', ResolveIssueAction)

    # Waits until action server has started up and started listening for goals
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = ResolveIssueGoal()  # creates a goal to send to the action server
    goal.issue = 'lostPerson'

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    result = client.get_result()

    return result

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('resolveIssue_client')
        result = ResolveIssue_client()
        print "Result:", result.sayResolved
        # rospy.spin()  # Maintain the service open
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")




# import rospy
# # Import the service message python classes generated from Empty.srv
# from std_srvs.srv import Empty, EmptyResponse
#
# def my_callback(request):
#   print “my_callback has been called”
#   # The service Response class, in this case EmptyResponse
#   return EmptyResponse()
#
# rospy.init_node('service_server')
# # Creates a service called /my_service with the defined callback
# my_service = rospy.Service('/my_service', Empty, my_callback)
# rospy.spin()  # Maintain the service open

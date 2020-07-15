#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: conv2scrn_client.py
# Author: Cecilia Aponte
'''

# Uncomment lines 10, 13, 15 if you're running this node in its own separate
# terminal window. Otherwise the script will immediately exit and its terminal window will close.
import rospy
# Brings in the SimpleActionClient
import actionlib
from er_action_msgs.msg import SayAction, SayGoal, SayResult, SayFeedback



def conv2scrn_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('conv2screen_as', SayAction)

    # Waits until action server has started up and started listening for goals
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = SayGoal()  # creates a goal to send to the action server
    goal.command = 'welcome'

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
        rospy.init_node('conv2scrn_client')
        result = conv2scrn_client()
        print "Result:", result.conversation
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

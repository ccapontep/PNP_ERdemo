#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: print_to_screen.py
# Author: Cecilia Aponte
'''

# Uncomment lines 10, 13, 15 if you're running this node in its own separate
# terminal window. Otherwise the script will immediately exit and its terminal window will close.
import rospy
# Brings in the SimpleActionClient
import actionlib

def conv2scrn_server(request):
    # rospy.init_node('print_to_screen', anonymous=True)
    print("Please keep this running in a separate tab.")
    # rospy.spin() # Maintain the service open
    return EmptyResponse()

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()


rospy.init_node('print_to_screen')
# Creates a service called /my_service with the defined callback
communicate2screen = rospy.Service('/communicate2screen', Empty, conv2scrn_server)
rospy.spin()  # Maintain the service open

# if __name__ == '__main__':
#     main()



def conv2scrn_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('er_action_msgs', SayAction)

    # Waits until action server has started up and started listening for goals
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = SayGoal()  # creates a goal to send to the action server


    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('print_to_screen')
        result = conv2scrn_client()
        print("Result:", result.result)
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

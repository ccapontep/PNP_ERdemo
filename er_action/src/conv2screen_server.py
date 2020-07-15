#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: conv2screen_server.py
# Author: Cecilia Aponte
'''

# Uncomment lines 10, 13, 15 if you're running this node in its own separate
# terminal window. Otherwise the script will immediately exit and its terminal window will close.
import rospy
# Brings in the SimpleActionClient
import actionlib
from er_action_msgs.msg import SayAction, SayResult#, SayFeedback#, SayGoal


class Conv2screen_Server():

    def __init__(self):
        self.c2s_server = actionlib.SimpleActionServer("conv2screen_as", SayAction, execute_cb=self.action_cb, auto_start=False)
        self.c2s_server.start()

    def action_cb(self, goal):

        result = SayResult()
        # feedback = SayFeedback()
        success = True


        if goal.command == 'welcome':
            if self.c2s_server.is_preempt_requested(): success = False
            result.conversation = 'Hello, how can I help you?'

        if success == True:
            self.c2s_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('conv2screen_server')
    s = Conv2screen_Server()
    rospy.spin()


# def conv2screen_server(request):
#     # rospy.init_node('print_to_screen', anonymous=True)
#     print("Please keep this running in a separate tab.")
#     # rospy.spin() # Maintain the service open
#     return EmptyResponse()
#
# def conv2screen_server():
#
#     s = rospy.Service('add_two_ints', Empty, conv2screen_server)
#     print("Please keep this running in a separate tab.")
#     rospy.spin() # Maintain the service open

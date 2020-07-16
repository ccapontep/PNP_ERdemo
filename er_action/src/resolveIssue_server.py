#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: resolveIssue_server.py
# Author: Cecilia Aponte
'''

import rospy
import actionlib
from er_action_msgs.msg import ResolveIssueAction, ResolveIssueResult#, ResolveIssueFeedback#, ResolveIssueGoal


class ResolveIssue_Server():

    def __init__(self):
        self.dia_server = actionlib.SimpleActionServer("resolveIssue_as", ResolveIssueAction, execute_cb=self.action_cb, auto_start=False)
        self.dia_server.start()

    def action_cb(self, goal):

        result = ResolveIssueResult()
        # feedback = ResolveIssueFeedback()
        success = True


        if goal.issue == 'lostPerson':
            if self.dia_server.is_preempt_requested(): success = False
            result.sayResolved = 'Issue resolved.'
            print('I need you to walk slower, please.')

        if success == True:
            self.dia_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('resolveIssue_server')
    s = ResolveIssue_Server()
    rospy.spin()


# def resolveIssue_server(request):
#     # rospy.init_node('print_to_screen', anonymous=True)
#     print("Please keep this running in a separate tab.")
#     # rospy.spin() # Maintain the service open
#     return EmptyResponse()
#
# def resolveIssue_server():
#
#     s = rospy.Service('add_two_ints', Empty, resolveIssue_server)
#     print("Please keep this running in a separate tab.")
#     rospy.spin() # Maintain the service open

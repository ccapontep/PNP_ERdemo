#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: dialog_server.py
# Author: Cecilia Aponte
'''

import rospy
import actionlib
from er_action_msgs.msg import DialogAction, DialogResult#, DialogFeedback#, DialogGoal


class Dialog_Server():

    def __init__(self):
        self.dia_server = actionlib.SimpleActionServer("dialog_as", DialogAction, execute_cb=self.action_cb, auto_start=False)
        self.dia_server.start()

    def action_cb(self, goal):

        result = DialogResult()
        # feedback = DialogFeedback()
        success = True


        if goal.command == 'welcome':
            if self.dia_server.is_preempt_requested(): success = False
            result.conversation = 'Hello, how can I help you?'
            print('Hello, how can I help you?')

        if success == True:
            self.dia_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('dialog_server')
    s = Dialog_Server()
    rospy.spin()


# def dialog_server(request):
#     # rospy.init_node('print_to_screen', anonymous=True)
#     print("Please keep this running in a separate tab.")
#     # rospy.spin() # Maintain the service open
#     return EmptyResponse()
#
# def dialog_server():
#
#     s = rospy.Service('add_two_ints', Empty, dialog_server)
#     print("Please keep this running in a separate tab.")
#     rospy.spin() # Maintain the service open

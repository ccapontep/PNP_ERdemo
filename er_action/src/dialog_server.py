#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: dialog_server.py
# Author: Cecilia Aponte
'''

import rospy
import actionlib
from er_action_msgs.msg import DialogAction, DialogResult, DialogFeedback #, DialogGoal

class Dialog_Server():

    def __init__(self):
        self.dia_server = actionlib.SimpleActionServer("dialog_as", DialogAction, execute_cb=self.action_cb, auto_start=False)
        self.dia_server.start()

    def action_cb(self, goal):

        result = DialogResult()
        feedback = DialogFeedback()

        if goal.command == 'welcome':
            if self.dia_server.is_preempt_requested():
                success = False
                # break

            dialog_output = ['\nStarting dialog..\n',
                            '\tRobot: Hello, I will be asking some questions to get the data of your health concern.\n',
                            '\tPerson: Yes, thank you.\n',
                            '..finalized dialog\n',
                            '--------------\n',
                            'Done']

            for i, output in enumerate(dialog_output):
                if output != 'Done':
                    feedback.conversation = output
                    print(feedback.conversation)
                    self.dia_server.publish_feedback(feedback)

            result.result = 'Conversation finalized.'
            success = True

        if success == True:
            self.dia_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('dialog_server')
    s = Dialog_Server()
    rospy.spin()

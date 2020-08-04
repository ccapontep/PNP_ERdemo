#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: resolveIssue_server.py
# Author: Cecilia Aponte
'''

import rospy
import actionlib
from er_action_msgs.msg import ResolveIssueAction, ResolveIssueResult, ResolveIssueFeedback #, ResolveIssueGoal

class ResolveIssue_Server():

    def __init__(self):
        self.resolve_server = actionlib.SimpleActionServer("resolveIssue_as", ResolveIssueAction, execute_cb=self.action_cb, auto_start=False)
        self.resolve_server.start()

    def action_cb(self, goal):

        result = ResolveIssueResult()
        feedback = ResolveIssueFeedback()

        if goal.issue == 'lostperson':
            if self.resolve_server.is_preempt_requested():
                success = False
                # break
            dialog_output = ['\nStarting to resolve the issue: %s..\n' % goal.issue,
                            '\tRobot: I need you to walk slower, please.\n',
                            '\tPerson: Sorry, I will.\n',
                            '..finalized dialog to resolve\n',
                            '--------------\n',
                            'Done']

            for i, output in enumerate(dialog_output):
                if output != 'Done':
                    feedback.conversation = output
                    print(feedback.conversation)
                    self.resolve_server.publish_feedback(feedback)

            result.sayResolved = 'Issue resolved.'
            success = True

        if success == True:
            self.resolve_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('resolveIssue_server')
    s = ResolveIssue_Server()
    rospy.spin()

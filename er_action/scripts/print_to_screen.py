#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
# Name: print_to_screen.py
# Author: Cecilia Aponte
'''

# Uncomment lines 10, 13, 15 if you're running this node in its own separate
# terminal window. Otherwise the script will immediately exit and its terminal window will close.
import rospy

def print2screen():
    rospy.init_node('print_to_screen', anonymous=True)
    print("Please keep this running in a separate tab.")
    rospy.spin() # Maintain the service open

if __name__ == '__print2screen__':
    print2screen()



import rospy
# Import the service message python classes generated from Empty.srv
from std_srvs.srv import Empty, EmptyResponse

def my_callback(request):
  print “my_callback has been called”
  # The service Response class, in this case EmptyResponse
  return EmptyResponse()

rospy.init_node('service_server')
# Creates a service called /my_service with the defined callback
my_service = rospy.Service('/my_service', Empty, my_callback)
rospy.spin()  # Maintain the service open

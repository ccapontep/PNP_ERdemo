#!/bin/bash
# Use: ./start_demo.bash

xterm -e roslaunch er_demo dis-B1.launch &
sleep 5
xterm -e roslaunch rp_action robot.launch &
sleep 5
xterm -e roslaunch er_pnp robot_plan.launch &




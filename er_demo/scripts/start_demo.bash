#!/bin/bash
# Use: ./start_demo.bash

xterm -e roslaunch er_demo dis-B1.launch &
#xterm -e roslaunch er_demo ER_planfloor.launch &
sleep 5
#xterm -e roslaunch rp_action robot.launch &
xterm -e roslaunch er_action robot.launch &
sleep 5
xterm -e roslaunch er_pnp robot_plan.launch &




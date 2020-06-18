#!/bin/bash
# Use: ./start_demo.bash [multirobot]

if [ "$#" == 0 ]; then

xterm -e roslaunch er_demo dis-B1.launch &
sleep 5
xterm -e roslaunch er_action robot.launch &
sleep 5
xterm -e roslaunch er_pnp robot_plan.launch &

else

# Launch multi-robot demo

ARG_MULTIROBOT="multirobot:=true"

xterm -e roslaunch er_demo dis-B1.launch $ARG_MULTIROBOT &
sleep 3
xterm -e roslaunch er_action robot.launch robotname:=robot_0 $ARG_MULTIROBOT &
sleep 3
xterm -e roslaunch er_pnp robot_plan.launch robotname:=robot_0 $ARG_MULTIROBOT &
sleep 3
xterm -e roslaunch er_action robot.launch robotname:=robot_1 $ARG_MULTIROBOT &
sleep 3
xterm -e roslaunch er_pnp robot_plan.launch robotname:=robot_1 $ARG_MULTIROBOT &

fi



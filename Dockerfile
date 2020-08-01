
FROM ub1604_kinetic_pnp:1.0

### PNP packages ###

USER root

RUN apt-get update && \
    apt-get install -y ros-kinetic-rviz

USER robot

ADD er_pnp /home/robot/src/er_pnp
ADD er_demo /home/robot/src/er_demo
ADD er_pddl /home/robot/src/er_pddl
ADD er_action /home/robot/src/er_action
ADD er_action_msgs /home/robot/src/er_action_msgs

RUN cd $HOME/ros/catkin_ws/src && \
    ln -s $HOME/src/er_action . && \
    ln -s $HOME/src/er_action_msgs . && \
    ln -s $HOME/src/er_pnp . && \
    ln -s $HOME/src/er_demo .

# Compile ROS packages

RUN /bin/bash -ci "cd $HOME/ros/catkin_ws; catkin_make -j1"


# Set working dir and container command

WORKDIR /home/robot

CMD /usr/bin/tmux




FROM ub1604_kinetic_pnp:0.1

### PNP packages ###

USER robot

ADD er_pnp /home/robot/src/er_pnp
ADD er_demo /home/robot/src/er_demo

RUN cd $HOME/ros/catkin_ws/src && \
    ln -s $HOME/src/er_pnp . && \
    ln -s $HOME/src/er_demo .

# Compile ROS packages

RUN /bin/bash -ci "cd $HOME/ros/catkin_ws; catkin_make -j1"


# Set working dir and container command

WORKDIR /home/robot

CMD /usr/bin/tmux



#!/bin/bash

# Use  ./run.bash [version]

IMAGENAME=ub1604_kinetic_pnp_demo_er

VERSION=0.1
if [ ! "$1" == "" ]; then
  VERSION=$1
fi

# change setings here if needed
PLAYGROUND_FOLDER=$HOME/playground
PNP_FOLDER=$HOME/src/PetriNetPlans
ERPNP_FOLDER=`pwd`


echo "Running image $IMAGENAME:$VERSION ..."

if [ -d /usr/lib/nvidia-384 ]; then
  NVIDIA_STR="-v /usr/lib/nvidia-384:/usr/lib/nvidia-384 \
           -v /usr/lib32/nvidia-384:/usr/lib32/nvidia-384 \
           --device /dev/dri"
  echo "Nvidia support enabled"
fi

docker run -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/.Xauthority:/home/robot/.Xauthority:rw \
    $NVIDIA_STR \
    -e DISPLAY=$DISPLAY \
    --privileged \
    --net=host \
    -v $PLAYGROUND_FOLDER:/home/robot/playground \
    -v $PNP_FOLDER:/home/robot/src/PetriNetPlans \
    -v $ERPNP_FOLDER/er_pnp:/home/robot/src/er_pnp \
    -v $ERPNP_FOLDER/er_demo:/home/robot/src/er_demo \
    -v $ERPNP_FOLDER/er_pddl:/home/robot/src/er_pddl \
    $IMAGENAME:$VERSION



#!/bin/bash

# Use  ./build.bash [Dockerfile] [version]

IMAGENAME=pnp_er_demo

DOCKERFILE=Dockerfile
if [ ! "$1" == "" ]; then
  DOCKERFILE=$1
fi

VERSION=latest
if [ ! "$2" == "" ]; then
  VERSION=$2
fi

docker build --no-cache -t $IMAGENAME:$VERSION -f $DOCKERFILE .


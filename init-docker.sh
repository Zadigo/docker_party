#!/bin/bash

KERNEL_INFO=uname -s
SYSTEM_INFO=uname -m
COMPOSE_VERSION="1.25.0"
URL_FOR_COMPOSE="https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-$KERNEL_INFO-$SYSTEM_INFO"

# Installs docker
sudo apt-get install docker.io
# Installs docker compose
sudo curl -L $URL_FOR_COMPOSE -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Updates docker engine
# apt-get upgrade docker-engine

# General update
apt-get update
apt-get upgrade

# Prints Docker version
# echo docker version | grep "Version"

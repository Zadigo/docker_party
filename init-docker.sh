#!/bin/bash

# Installs docker
sudo apt-get install docker.io
# Installs docker compose
# sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
# docker-compose run test

# Updates docker engine
# apt-get upgrade docker-engine

# Prints Docker version
# echo docker version | grep "Version"

read -p "Install nginx-proxy [yes|no]? " install_nginx_proxy

if [ $install_nginx_proxy = "yes" ]; then
    # Create a network for nginx-proxy
    docker network create nginx-proxy
    # Install nginx-proxy: this is a container that allows to process
    # multiple incoming requests and redirect them to the correct container.
    # Useful in cases where we want to host multiple websites using the same
    # VPS and IP adress
    docker run -d -p 80:80 --name nginx-proxy --net nginx-proxy -v /var/run/docker.sock:/tmp/docker.sock jwilder/nginx-proxy
fi

# Pulls the cadvisor container for monitoring purposes
# read -p "Install Cadvisor [yes|no]?" install_cadvisor

# if [ $cadvisor = "yes" ]; then
#     docker pull cadvisor
# fi

# Pulls the PGAdmin container
# read -p "Install PG Admin [yes|no]?" install_cadvisor

# if [ $cadvisor = "yes" ]; then
#     docker pull dpage/pgadmin4
# fi

# Install tree
snap install tree

# General update
sudo apt-get update
sudo apt-get upgrade

# Firewall
sudo ufw enable
sudo ufw allow http
sudo ufw allow https

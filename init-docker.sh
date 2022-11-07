#!/bin/bash

# Installs docker
sudo apt-get install docker.io
# Installs docker compose
# sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
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

# sudo chown ubuntu:ubuntu -R /usr/local/lib/
# sudo snap install node --classic --channel=19
# npm -g add @vue/cli

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
sudo ufw allow 22

# Github
read -p "Git username:" username
git config --global user.name $username
read -p "Git email:" email
git config --global user.email $email

# Change ownership of the home directory
# which can throw a permission denied error
# when trying to clone a git directory
# sudo chown ubuntu:ubuntu -R home
# Do the same thing for the Docker sock which
# can also throw a permission error
# sudo chown ubuntu:ubuntu -R /var/run/docker.sock
# read -p "Clone git directory [yes/no]?" clone_git

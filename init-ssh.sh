#!/bin/bash/

# A script that initializes an SSH
# key on the server and facilitates
# for example pull and push without
# password

EMAIL=""

ssh-keygen -t rsa -b 4096 -C $EMAIL

eval $(ssh-agent -s)

ssh-add ~/.ssh/id_rsa

# Test connection
ssh -T git@github.com

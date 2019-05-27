# docker_party
Python test applications and items related to docker


# SSH
[https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html]
## Windows
1. Open git bash
2. ssh-keygen
3. eval $(ssh-agent)
4. ssh-add ~/.ssh/id_rsa.pub
5. Add the public key to your Bitbucket settings
6. ssh -T git@bitbucket.org

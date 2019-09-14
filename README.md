# docker_party
Python test applications and items related to docker


# SSH Windows

[https://confluence.atlassian.com/bitbucket/set-up-an-ssh-key-728138079.html]
## Windows
1. Open git bash
2. ssh-keygen -t rsa -b 4096 -C "email"
3. eval "$(ssh-agent -s)"
4. ssh-add ~/.ssh/id_rsa
5. Add the public key to your Bitbucket settings
6. ssh -T git@bitbucket.org

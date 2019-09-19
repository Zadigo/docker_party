#!/usr/bin/python

import argparse
import os
import pathlib
import posixpath
from subprocess import Popen, STDOUT

import requests

class Certificates:
    def __init__(self, domains=[]):
        # current_path = posixpath.curdir
        # Path that contains the live domains
        # to be used with letsencrypt
        live_domains_path = '/etc/letsencrypt/conf/live'
        if not self._exists(live_domains_path):
            for domain in domains:
                os.makedirs(os.path.join(live_domains_path, domain))

        params = " openssl req -x509 -nodes -newkey rsa:1024 -days 1"\
                    "-keyout /data/certbot/privkey.pem -out /data/certbot/fullchain.pem -subj '/CN=localhost'"
        statement = 'docker-compose run --rm --entrypoint' + params + ' certbot'
        result = Popen(statement, stdout=STDOUT)
        print(result)
        

    @staticmethod
    def _exists(path):
        return posixpath.exists(path)
        

certificates = Certificates(domains=['nawoka.fr', 'www.nawoka.fr'])

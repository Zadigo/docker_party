#!/usr/bin/python

import os
import pathlib
import posixpath

import requests


class Certificates:
    def get_certificates(self, create_to='/home/certificates/'):
        urls = [
            # "https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf",
            "https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem"
        ]
        
        for url in urls:
            try:
                response = requests.get(url)
            except requests.HTTPError:
                raise
            else:
                if response.status_code == 200:
                    data = response.content
                else:
                    print(f"Could not get content for {url}")
                    raise Exception()
            
            file_name = os.path.basename(url)
            certificate_path = posixpath.join(create_to, file_name)

            # Objectify the paths in order
            # to perform other quick operations
            # if necessary
            paths = []
            paths.append(pathlib.PosixPath(certificate_path))
            
            # Write the certificates -- ready
            # to be used elsewhere
            with open(certificate_path, 'w') as f:
                f.write(data)
        return paths

    @staticmethod
    def get_file_name(url):
        return os.path.basename(url)

class LetsEncrypt(Certificates):
    def __init__(self, **kwargs):
        current_path = kwargs['start_path'] or posixpath.curdir
        certificates_dir = posixpath.join(current_path, 'certificates')
        # Check if we have a folder to
        # store the different certificates
        certificate_path_exists = posixpath.lexists(certificates_dir)

        # Create the corresponding path
        if not certificate_path_exists:
            os.mkdir(certificates_dir)

        # certificates
        paths = self.get_certificates()
        
        print(paths[0].exists())

encrypt = LetsEncrypt(start_path='/home/')

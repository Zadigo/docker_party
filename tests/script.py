#!/usr/bin/python

import argparse
import os
import pathlib
import posixpath

import requests

# class TLSError(Exception):
#     def __init__(self, message=None, url=None):
#         self.message = "Could not get content for %s" % url

#     def __unicode__(self):
#         return self.message

#     def __repr__(self):
#         return self.__unicode__()

class TLS:
    def download_parameters(self, create_to='/home/tls_parameters/'):
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
                    print("Could not get content for %s" % url)
                    # raise TLSError(url=url)
                    raise Exception()
            
            file_name = os.path.basename(url)
            certificate_path = posixpath.join(create_to, file_name)

            # Objectify the paths in order
            # to perform other quick operations
            # if necessary
            paths = []
            paths.append(pathlib.PosixPath(certificate_path))
            
            # Write the parameters -- ready
            # to be used elsewhere
            with open(certificate_path, 'wb') as f:
                f.write(data)
        return paths

    @staticmethod
    def get_file_name(url):
        return os.path.basename(url)

class LetsEncrypt(TLS):
    def __init__(self, **kwargs):
        current_path = kwargs['start_path'] or posixpath.curdir
        tls_parameters_dir = posixpath.join(current_path, 'tls_parameters')
        # Check if we have a folder to
        # store the different certificates
        certificate_path_exists = posixpath.lexists(tls_parameters_dir)

        # Create the corresponding path
        if not certificate_path_exists:
            os.mkdir(tls_parameters_dir)

        # certificates
        paths = self.download_parameters()
        
        for path in paths:
            if path.exists():
                print('+ Created TLS parameter in %s' % path.as_posix())

encrypt = LetsEncrypt(start_path='/home/')

# if __name__ == "__main__":
#     args = argparse.ArgumentParser(description='Download TLS parameters for Cerbot')
#     args.add_argument('-p', '--start', help='Starting path to download and create the parameter directory')
#     parsed_args = args.parse_args()

#     encrypt = LetsEncrypt(start_path=parsed_args.start)

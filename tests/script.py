#!/usr/bin/python

import posixpath

class Requestor:
    pass

class LetsEncrypt(Requestor):
    def __init__(self, **kwargs):
        current_path = kwargs['start_path'] or posixpath.curdir
        certificates_dir = posixpath.join(current_path, 'certificates')
        # Check if we have a folder to
        # store the different certificates
        certificate_path_exists = posixpath.lexists(certificates_dir)

        print(certificate_path_exists)

encrypt = LetsEncrypt(start_path='/home/')

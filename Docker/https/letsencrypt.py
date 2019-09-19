#!/bin/sh

print('Hello')

# import os
# import pathlib
# import posixpath
# import subprocess
# from threading import Thread

# DOMAINS = ['nawoka.fr', 'www.nawoka.fr']

# RSA_KEY_SIZE = 4096

# DATA_PATH = '/data/certbot'

# EMAIL = 'contact.nawoka@gmail.com'

# STAGING = 0

# class Requester:
#     pass

# class LetsEncrypt(Requester):
#     def __init__(self, **kwargs):
#         self.base_path = posixpath.curdir
#         path_exists = posixpath.lexists(DATA_PATH)

#         if path_exists:
#             # A certificate already exists
#             # and we need to replace it
#             print('Path not there')

#         # Check whether the required files are
#         # present in the folder of this path
#         # e.g. options-ssl-nginx.conf or
#         # ssl-dhparams.pem
#         conf_files = [
#             posixpath.join(DATA_PATH, 'options-ssl-nginx.conf'),
#             posixpath.join(DATA_PATH, 'ssl-dhparams.pem')
#         ]

#     @staticmethod
#     def path_exists(path, return_path=False):
#         if posixpath.lexists(path):
#             if return_path:
#                 return path
#             return True

#         if return_path:
#             return path
#         return False

# encrypt = LetsEncrypt(data_path='/data/certbot')

# thread1 = Thread(target=LetsEncrypt, name="Let's Encrypt")
# thread2 = Thread(target=Requester, name='Requester')
# thread1.start()
# thread2.start()

#!/usr/bin/python

import posixpath

class Requestor:
    pass

class LetsEncrypt(Requestor):
    def __init__(self):
        current_path = posixpath.curdir
        print(current_path)

encrypt = LetsEncrypt()
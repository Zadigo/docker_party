#!/usr/bin/python

import argparse
import os
import pathlib
import posixpath

import requests

class Certificates:
    def __init__(self):
        current_path = posixpath.curdir
        print(current_path)

certificates = Certificates()

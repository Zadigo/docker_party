#!/usr/bin/env python

import os

def test_something(func):
    def _test():
        is_true = func()
        if is_true:
            print('PRODUCTION')
        else:
            print('NOTHING')
    return _test()

@test_something
def run_something():
    return os.environ.get('PRODUCTION', None)

run_something

#!/usr/bin/env python

import os
import subprocess

a = os.environ.get('SCRIPT_TO_START')
b = os.environ.get('PRODUCTION')

print(a, b)

# obj = os.environ.get('SCRIPT_TO_START')
# if os.path.exists(obj):
#     os.chdir('/pages/')
#     subprocess.call(['/pages/start.py'], shell=True)

"$@"
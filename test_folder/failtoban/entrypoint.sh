#!/bin/bash

service fail2ban restart
fail2ban-client status

"$@"
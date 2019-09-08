FROM superitman/fail2ban

COPY custom.conf jaild.d/custom.conf

# Copy the filters in filter.d
COPY ./jails/ssh.conf ./filter.d

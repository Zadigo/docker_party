FROM superitman/fail2ban

COPY custom.conf jail.d/custom.conf

# Copy the filters in filter.d
COPY ./jails/sshd.conf filter.d

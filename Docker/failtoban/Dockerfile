FROM superitman/fail2ban

ENV bantime=3600
ENV findtime=3600
ENV default_maxretry=6
ENV destemail=contact.kurrikulam@gmail.com

COPY ./jails/jail.local etc/fail2ban/

COPY ./jails/nginx-http-auth.conf etc/fail2ban/filter.d/
# COPY ./jails/nginx-badbots.conf etc/fail2ban/filter.d/
# COPY ./jails/nginx-noproxy.conf etc/fail2ban/filter.d/
# COPY ./jails/nginx-noscript.conf etc/fail2ban/filter.d/

COPY ./init/entrypoint.sh start_protection/
RUN chmod +x ./start_protection/entrypoint.sh

ENTRYPOINT [ "./start_protection/entrypoint.sh" ]
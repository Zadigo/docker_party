FROM superitman/fail2ban

ENV bantime=3600
ENV findtime=3600
ENV default_maxretry=6
ENV destemail=contact.kurrikulam@gmail.com

COPY jail.local etc/fail2ban/

COPY nginx-badbots.conf etc/fail2ban/filter.d/
COPY nginx-http-auth.conf etc/fail2ban/filter.d/
COPY nginx-noproxy.conf etc/fail2ban/filter.d/
COPY nginx-noscript.conf etc/fail2ban/filter.d/

# RUN  ls -la etc/fail2ban/
RUN touch var/log/auth.log
# RUN  ls -la var/log/

COPY entrypoint.sh start_protection/
RUN chmod +x ./start_protection/entrypoint.sh

ENTRYPOINT [ "./start_protection/entrypoint.sh" ]
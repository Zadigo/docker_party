FROM certbot/certbot

COPY init-letsencrypt.sh .

RUN chmod +x init-letsencrypt.sh

ENTRYPOINT [ "./init-letsencrypt.sh" ]
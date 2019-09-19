FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

RUN ls -la

# COPY init-letsencrypt.sh .

# ENTRYPOINT [ "./init-letsencrypt.sh" ]
FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

# COPY init-letsencrypt.sh .

ENTRYPOINT [ "/opt/certbot/letsencrypt.py" ]

# /usr/bin/python

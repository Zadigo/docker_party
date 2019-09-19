FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

RUN readlink -f letsencrypt.py

# COPY init-letsencrypt.sh .

ENTRYPOINT [ "/src/letsencrypt.py" ]

# /usr/bin/python

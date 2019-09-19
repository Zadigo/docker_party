FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

# COPY init-letsencrypt.sh .

# ENTRYPOINT [ "letsencrypt.py" ]
CMD [ "/bin/bash", "-l", "letsencrypt.py" ]

# /usr/bin/python

FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

RUN apt install tree

RUN tree -d

# COPY init-letsencrypt.sh .

# ENTRYPOINT [ "./init-letsencrypt.sh" ]

# /usr/bin/python

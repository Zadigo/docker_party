FROM python:3 AS base

RUN pip install requests

ENV START_PATH=/home

ENV TLS_PARAMETERS=/home/tls_parameters

COPY script.py ${START_PATH}

RUN chmod +x ${START_PATH}/script.py

ENTRYPOINT [ "/usr/bin/python", "/home/script.py" ]

# FROM certbot:certbot AS construct

# ENV CERTBOT_CONF=/data/certbot/conf

# COPY from=base ${TLS_PARAMETERS}/options-ssl-nginx.conf ${CERTBOT_CONF}

# COPY from=base ${TLS_PARAMETERS}/ssl-dhparams.pem ${CERTBOT_CONF}

FROM python:3 AS base

RUN pip install requests

ENV START_PATH=/home

COPY script.py ${START_PATH}

RUN chmod +x ${START_PATH}/script.py

ENTRYPOINT [ "python", "/home/script.py" ]


FROM certbot/certbot:latest AS construct

ENV CERTBOT_CONF=/data/certbot/conf

# COPY from=base ${TLS_PARAMETERS}/options-ssl-nginx.conf ${CERTBOT_CONF}

COPY --from=base /home/tls_parameters/ssl-dhparams.pem ${CERTBOT_CONF}

RUN ls
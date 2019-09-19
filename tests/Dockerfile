FROM python:3 AS base

RUN pip install requests

ENV START_PATH=/home

COPY script.py ${START_PATH}

RUN chmod +x ${START_PATH}/script.py

RUN mkdir ${START_PATH}/tls_parameters

RUN python /home/script.py



FROM certbot/certbot:latest AS construct

ENV BASE_PATH=/opt/certbot

ENV CERTBOT_CONF_PATH=../../data/certbot/conf

COPY --from=base /home/tls_parameters ${CERTBOT_CONF_PATH}

RUN cd ../../.. && ls

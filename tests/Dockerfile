# FROM ubuntu:latest

# RUN apt install python 3

# RUN export PYTHON=/usr/bin/python &&\
#     export PATH=$PATH:$PYTHON

# RUN apt update &&\
#     apt upgrade

# COPY script.py ./home

# RUN chmod +x ./home/script.py

# ENTRYPOINT [ "bash" ]

FROM python:3

ENV START_PATH=/home

ENV CERTBOT_DATA_PATH=/data/certbot

COPY script.py /scripts/

RUN chmod +x ${START_PATH}/scripts.py
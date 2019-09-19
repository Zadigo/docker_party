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

COPY script.py /scripts/

RUN chmod +x /scripts/scripts.py
FROM ubuntu:latest

RUN apt update &&\
    apt upgrade

# RUN apt install python

COPY script.py ./home

RUN chmod +x ./home/script.py

# ENTRYPOINT [ "bash" ]

FROM ubuntu:latest

# RUN apt install python 3

RUN apt update &&\
    apt upgrade

COPY script.py ./home

RUN chmod +x ./home/script.py

# ENTRYPOINT [ "bash" ]

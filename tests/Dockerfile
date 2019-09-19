FROM ubuntu:latest

RUN apt update &&\
    apt upgrade

COPY script.py ./home

RUN chmod +x ./home/script.py

WORKDIR /home

ENTRYPOINT [ "script.py" ]
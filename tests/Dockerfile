FROM certbot/certbot:latest AS construct

ENV BASE_PATH=../..

COPY script.py /home

RUN chmod +x /home/script.py

RUN python /home/script.py

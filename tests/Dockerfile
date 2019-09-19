FROM certbot/certbot:latest AS construct

ENV BASE_PATH=../..

COPY script.py /home

COPY other.sh /home/other.sh

RUN chmod +x /home/script.py

RUN python /home/script.py

RUN /bin/bash other.sh

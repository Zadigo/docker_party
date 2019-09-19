FROM certbot/certbot:latest AS construct

ENV HOME=/home

ENV LIVE_DOMAINS_PATH=/etc/letsencrypt/live

RUN mkdir ${LIVE_DOMAINS_PATH}/nawoka.fr &&\
    mkdir ${LIVE_DOMAINS_PATH}/www.nawoka.fr

COPY script.py ${HOME}

RUN chmod +x ${HOME}/script.py

RUN python ${HOME}/script.py

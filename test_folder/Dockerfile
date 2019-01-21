FROM python:3

ARG SCRIPT_TO_START
ARG PRODUCTION

COPY ./start.py /pages/
COPY ./start.sh /entries/

RUN chmod +x ./entries/start.sh && \
    chmod +x ./pages/start.py

EXPOSE 8000

ENTRYPOINT [ "./entries/start.sh" ]

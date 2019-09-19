FROM certbot/certbot

COPY letsencrypt.py .

RUN chmod +x letsencrypt.py

RUN cd src && ls

RUN echo "----"

RUN cd .. && cd .. && ls

# COPY init-letsencrypt.sh .

# ENTRYPOINT [ "./init-letsencrypt.sh" ]
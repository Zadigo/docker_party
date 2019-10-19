FROM postgres:latest

LABEL "com.postgres.app"="postgres"

# Pg_cron extension
# RUN apt-get update
# RUN sudo apt-get -y install postgresql-10-cron

RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/postgresql.conf

EXPOSE 5432

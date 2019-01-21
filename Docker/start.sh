#!/bin/bash

function manage_app () {
    python manage.py makemigrations
    python manage.py migrate
}

function start_development() {
    # manage_app
    python manage.py runserver 0.0.0.0:8000
}

function start_production() {
    gunicorn kurrikulam.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code/kurrikulam --log-file -
}

if [ ${PRODUCTION} == "false" ]; then
    # use development server
    start_development
else
    # use production server
    start_production
fi
#!/bin/bash

function start_development() {
    python manage.py runserver 0.0.0.0:8000
}

function start_production() {
    gunicorn mydjango.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code/website/mydjango --log-file -
}

if [ ${PRODUCTION} == "false" ]; then
    # use development server
    start_development
else
    # use production server
    start_production
fi

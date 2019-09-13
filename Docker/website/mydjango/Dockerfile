FROM python:3

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

LABEL "com.example.vendor"="application"

COPY start.sh /start/

# COPY ./docker/wait_for_postgres.py /start/

RUN chmod +x ./start/start.sh
    # chmod +x ./start/wait_for_postgres.py

RUN mkdir /code

WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile

COPY Pipfile.lock Pipfile.lock

RUN pip3 install pipenv

RUN pipenv install --deploy --system

# Copy the application
COPY . /code/

EXPOSE 8000

RUN ls && cd .. && echo '---' && ls

# Start project using a simple script file
# ENTRYPOINT [ "../start/start.sh" ]
# ...or one that waits for the database
# ENTRYPOINT [ "../start/wait_for_postgres.py" ]
# ...or with development server
ENTRYPOINT [ "pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD pipenv run python manage.py runserver 0.0.0.0:8000
# ...or Gunicorn for production purposes
# CMD gunicorn kurrikulam.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code/kurrikulam --log-file -

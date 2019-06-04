# Installing Docker
```
sudo apt install docker.io
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
apt-get upgrade docker-engine
docker info
```

# Translation
You need to install [http://www.gettext.com](GetText).
```
django-admin makemessages --locale=en
django-admin compilemessages --locale=en
```

# Migrations
```
docker-compose run <service> python /code/manage.py migrate --noinput
docker-compose run <service> python /code/manage.py createsuperuser
docker-compose run <service> python /code/manage.py collectstatic
```

__NOTE:__ Container has to be already running
```
docker start <container>
docker-compose exec <service> python manage.py makemigrations
docker-compose exec <service> python manage.py migrate
```

# Container management
Show containers.
```
docker ps
docker ps -a
```

## Connect inside database
```
~~docker-compose up~~
docker start postgres_database
docker exec -it postgres_database psql -U postgres
```

### Creating users or tables
```
CREATE USER ... WITH ENCRYPTED PASSWORD '...';

CREATE DATABASE ... OWNER ...;

GRANT ALL PRIVILEGES ON DATABASE ... TO ...;
```

# Static files
Push static files to AWS servers:
```
docker-compose exec <service> python manage.py collectstatic
```

# Build specific container
```
docker-compose -f docker-compose.prod.yml build
```

# Copy a file to local to edit or watch it
```
docker cp job_startup:/code/offres/migrations/0005_auto_20190204_1554.py .
```


docker images
docker run image
docker run -i -t image
docker logs container
docker run -it -p 8000:8000 -v /home/octo-train/kurrikulam/manage.py 0e1d5725479f
docker run -i -t -p 3000:3000 0e1d5725479f

docker run --rm -it -p 3000:3000 0e1d5725479f -v code:/home/octo-train/kurrikulam/

docker run -d -p 3000:3000 0e1d5725479f

docker run -p 8000:80 kurrikulam_jobsite jobsite
docker run -p 8000:80 kurrikulam_enginx
docker run --name jobsite --entrypoint /bin/bash kurrikulam_jobsite -c "ls -l /; id"
docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=Constance97170 -e POSTGRES_DB=job_database1 kurrikulam_db


docker-compose config
docker-compose rm
docker-compose run service
docker-compose images -a

docker ps -aq
docker container prune
docker rmi

exit()

docker container port job_startup

sudo apt get update
sudo apt get upgrade

docker rmi $(docker images -q --filter "dangling=true")

sudo nginx -s stop


Migrations issues


docker ps -aq --no-trunc -f status=exited | xargs docker rm

docker images -q --filter dangling=true | xargs docker rmi

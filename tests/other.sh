path = "data/certbot"


docker-compose run --rm --entrypoint "\
    openssl req -x509 -nodes -newkey rsa:1024 -days 1\
    -keyout '$path/privkey.pem' \
    -out '$path/fullchain.pem' \
    -subj '/CN=localhost'" certbot

echo "+ Starting nginx ..."
docker-compose up --force-recreate -d nginx
echo

echo "+ Deleting dummy certificate ..."

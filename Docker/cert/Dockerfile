FROM certbot/certbot

LABEL "com.cerbot.letsencrypt"="certbot"

CMD [ "certonly", "--manual", "-d example.com", "-d *.example.com", "--preferred-challenges", "dns-01", "--server", "https://acme-v02.api.letsencrypt.org/directory" ]

ENTRYPOINT [ "certbot" ]

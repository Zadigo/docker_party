FROM nginx

LABEL "com.nginx.app"="nginx"

COPY ./http/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

CMD [ "nginx", "-g", "daemon off;" ]
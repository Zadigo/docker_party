FROM nginx

# Replace default nginx.conf
RUN rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
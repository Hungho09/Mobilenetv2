FROM nginx:alpine

# Copy static files to nginx html directory
COPY . /usr/share/nginx/html

# Expose port 4200 (as requested in docker-compose)
RUN sed -i 's/80/4200/g' /etc/nginx/conf.d/default.conf

EXPOSE 4200

CMD ["nginx", "-g", "daemon off;"]

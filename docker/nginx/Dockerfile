FROM nginx:1.13

RUN apt-get update && apt-get install -y nano

RUN deluser www-data
RUN adduser --disabled-password --no-create-home --uid 1000 --shell /bin/bash www-data

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
ADD ./uwsgi-params /etc/nginx/

#COPY ./dev.ecomx.loc.crt /etc/ssl/certs/dev.ecomx.loc.crt
#COPY ./dev.ecomx.loc.key /etc/ssl/private/dev.ecomx.loc.key
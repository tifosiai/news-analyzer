FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN mkdir -p /etc/ssl/
RUN chmod 755 /etc/ssl/

RUN chown -R root:root /etc/ssl/
COPY ./fullchain.pem /etc/ssl/
COPY ./privkey.pem /etc/ssl/

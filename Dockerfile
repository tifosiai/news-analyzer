FROM python:3.9-alpine

ENV PATH = "/script:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc g++ libc-dev linux-headers \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN apk del .tmp



RUN mkdir /app
COPY /src /app
RUN mkdir /app/staticfiles
COPY /script /app/script
RUN chmod +x /app/script/*


WORKDIR /app

COPY secrets.env /app


RUN adduser -D user
RUN chown -R user:user /app
RUN chown -R user:user /var
RUN chmod -R 755 /var/

RUN chmod +x script/entrypoint.sh

USER root

CMD ["/script/entrypoint.sh"]

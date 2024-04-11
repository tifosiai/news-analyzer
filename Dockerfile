FROM ubuntu:20.04

ENV PATH = "/script:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt install pip -y
RUN apt install libpq-dev -y
RUN apt install -y  gcc g++ libc-dev  \
    && apt-get install -y gcc python3-dev musl-dev \
    && apt install -y postgresql

RUN apt install build-essential -y
RUN apt install libpq-dev -y
RUN apt update
RUN python3 -m pip install --upgrade pip
RUN apt-get install -y libjpeg-dev zlib1g-dev 
RUN apt-get install libmysqlclient-dev -y
RUN python3 -m pip install --upgrade Pillow 
RUN apt install -y mysql-server  
RUN apt install -y python3.9
RUN python3 -m pip install --upgrade pip
RUN python3.9 -m pip install -r /requirements.txt
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

FROM python:3.10-slim

# ---------- for develop
COPY deploy/debian/sources.list.txt /etc/apt/sources.list
RUN pip config set global.index-url http://192.168.200.22:3141/root/pypi/+simple \
    && pip config set install.trusted-host 192.168.200.22
# ----------

COPY . /app
COPY ./pelican_publisher/pelican_publisher/settings/docker.py /app/pelican_publisher/pelican_publisher/settings/running.py
COPY deploy/supervisor/* /app/supervisor

RUN apt-get update \
    && apt-get install --yes redis-server \
    && mkdir /var/log/supervisor \
    && pip install --no-cache-dir -r /app/requirements/docker.txt \
    && mkdir /pp-output \
    && mkdir /pp-data

WORKDIR /app/pelican_publisher
EXPOSE 8000

VOLUME /pp-output
VOLUME /pp-data

RUN ./manage.py collectstatic --no-input

# TODO: nobody
CMD /etc/init.d/redis-server start \
    && supervisord -c  /app/supervisor/supervisord.conf \
    && ./manage.py migrate --no-input \
    && ./runserver.py -H 0.0.0.0

LABEL org.opencontainers.image.title="Pelican Publisher"
LABEL org.opencontainers.image.authors="Rex Zhang"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/ray1ex/pelican-publisher"
LABEL org.opencontainers.image.source="https://github.com/rexzhang/pelican-publisher"

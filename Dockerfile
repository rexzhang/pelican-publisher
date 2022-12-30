FROM python:3.11-alpine

ARG ENV
RUN if [ "$ENV" = "debug" ]; then echo "Change depends" \
    && pip config set global.index-url http://192.168.200.61:13141/root/pypi/+simple \
    && pip config set install.trusted-host 192.168.200.61 \
    # && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    ; fi

COPY pelican_publisher /app
COPY pelican_publisher/pelican_publisher/settings/docker.py /app/pelican_publisher/settings/running.py
COPY requirements /app/requirements
COPY deploy/docker/entrypoint.sh /app

RUN mkdir -p /etc/supervisor.d
COPY deploy/supervisor/conf.d/*.ini /etc/supervisor.d

RUN pip install --no-cache-dir -r /app/requirements/docker.txt \
    && apk add --no-cache redis supervisor \
    && mkdir /var/log/supervisor \
    && mkdir /pp-output \
    && mkdir /pp-data

EXPOSE 8000
VOLUME /pp-output
VOLUME /pp-data
WORKDIR /app

RUN ./manage.py collectstatic --no-input

# TODO: nobody
CMD ./entrypoint.sh

LABEL org.opencontainers.image.title="Pelican Publisher"
LABEL org.opencontainers.image.authors="Rex Zhang"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/ray1ex/pelican-publisher"
LABEL org.opencontainers.image.source="https://github.com/rexzhang/pelican-publisher"

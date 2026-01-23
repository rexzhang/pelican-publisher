FROM python:3.14-alpine

ARG ENV
ENV TZ="Asia/Shanghai"

RUN if [ "$ENV" = "rex" ]; then echo "Change depends" \
    && pip config set global.index-url http://192.168.200.26:13141/root/pypi/+simple \
    && pip config set install.trusted-host 192.168.200.26 \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    ; fi

COPY pelican_publisher /app/pelican_publisher
COPY pp_core /app/pp_core
COPY requirements /app/requirements
COPY manage.py /app/manage.py
COPY runserver.py /app/runserver.py

COPY deploy/docker/entrypoint.sh /app/entrypoint.sh
COPY deploy/supervisor/conf.d/*.ini /etc/supervisor.d/

RUN \
    # supervisor
    apk add --no-cache supervisor \
    # python depends
    && pip install --no-cache-dir -r /app/requirements/docker.txt \
    # cleanup --- \
    && rm -rf /root/.cache \
    && find /usr/local/lib/python*/ -type f -name '*.py[cod]' -delete \
    && find /usr/local/lib/python*/ -type d -name "__pycache__" -delete \
    # prepare django ---
    && mv /app/pelican_publisher/settings/docker.py /app/pelican_publisher/settings/running.py \
    # prepare path ---
    && mkdir /data \
    && mkdir /output \
    && mkdir /log

EXPOSE 8000
VOLUME /data
VOLUME /output
VOLUME /log

WORKDIR /app
RUN ./manage.py collectstatic --no-input

# TODO: nobody
CMD ./entrypoint.sh

LABEL org.opencontainers.image.title="Pelican Publisher"
LABEL org.opencontainers.image.authors="Rex Zhang"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/ray1ex/pelican-publisher"
LABEL org.opencontainers.image.source="https://github.com/rexzhang/pelican-publisher"

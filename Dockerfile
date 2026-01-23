FROM python:3.14-alpine

ARG BUILD_ENV
RUN if [ "$BUILD_ENV" = "rex" ]; then echo "Change depends" \
    && sed -i 's#https\?://dl-cdn.alpinelinux.org/alpine#https://mirrors.tuna.tsinghua.edu.cn/alpine#g' /etc/apk/repositories \
    && pip config set global.index-url https://proxpi.h.rexzhang.com/index/ \
    && pip config set install.trusted-host proxpi.h.rexzhang.com \
    ; fi

COPY requirements.d /app/requirements.d

RUN \
    # install python build depends ---
    apk add --no-cache --virtual .build-deps build-base libffi-dev \
    # --- build & install
    && pip install --no-cache-dir -r /app/requirements.d/docker.txt \
    # --- cleanup
    && apk del .build-deps \
    && rm -rf /root/.cache \
    && find /usr/local/lib/python*/ -type f -name '*.py[cod]' -delete \
    && find /usr/local/lib/python*/ -type d -name '__pycache__' -delete \
    # supervisor
    && apk add --no-cache supervisor


COPY pelican_publisher /app/pelican_publisher
COPY manage.py /app/manage.py
COPY runserver.py /app/runserver.py

COPY deploy/docker/entrypoint.sh /app/entrypoint.sh
COPY deploy/supervisor/conf.d/*.ini /etc/supervisor.d/

WORKDIR /app

RUN \
    # prepare path ---
    python manage.py collectstatic --no-input \
    && mkdir /data \
    && mkdir /output \
    && mkdir /log

EXPOSE 8000
VOLUME /data
VOLUME /output
VOLUME /log

ENV TZ=Asia/Shanghai
ENV DATABASE_URI=sqlite:///data/db.sqlite3
ENV ALLOWED_HOSTS='["*"]'
ENV PELICAN_WORKING_PATH=/tmp
ENV PELICAN_OUTPUT_PATH=/output

# TODO: nobody
CMD ./entrypoint.sh

LABEL org.opencontainers.image.title="Pelican Publisher"
LABEL org.opencontainers.image.authors="Rex Zhang"
LABEL org.opencontainers.image.url="https://hub.docker.com/repository/docker/ray1ex/pelican-publisher"
LABEL org.opencontainers.image.source="https://github.com/rexzhang/pelican-publisher"

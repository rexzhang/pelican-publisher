FROM python:3.8-slim

# ---------- TODO:develop env only
#COPY deploy/debian/sources.list.txt /etc/apt/sources.list
#RUN pip config set global.index-url http://host.docker.internal:3141/root/pypi/+simple/
#RUN pip config set install.trusted-host host.docker.internal
# ----------

COPY . /app
COPY ./pelican_publisher/pelican_publisher/settings/docker.py /app/pelican_publisher/pelican_publisher/settings/running.py

RUN apt-get update && apt-get install --yes supervisor redis-server iproute2 curl
COPY deploy/supervisor/*.conf /etc/supervisor/conf.d/

RUN pip install --no-cache-dir -r /app/requirements/docker.txt

WORKDIR /app/pelican_publisher
EXPOSE 8000

RUN mkdir /pp-output
RUN mkdir /pp-data
VOLUME /pp-output
VOLUME /pp-data

RUN ./manage.py collectstatic --no-input

# TODO: nobody
CMD /etc/init.d/redis-server start && /etc/init.d/supervisor start && ./manage.py migrate --no-input && ./runserver.py -H 0.0.0.0

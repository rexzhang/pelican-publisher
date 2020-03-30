FROM python:3

COPY . /app
#COPY ./pelican_publisher/pelican_publisher/settings/docker.py /app/pelican_publisher/pelican_publisher/settings/running.py

# TODO:develop env only
#COPY deploy/debian/sources.list.mirror.conf /etc/apt/sources.list

RUN apt-get update
RUN apt-get install --yes supervisor redis-server
COPY deploy/supervisor/web-server.conf /etc/supervisor/conf.d/

# TODO:develop env only
#RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/pelican_publisher
EXPOSE 8000

#RUN ./manage.py collectstatic --no-input

# TODO: nobody
#CMD ../scripts/fix-host-docker-internal-at-linux.sh && celery worker -A pelican_publisher

FROM python:3

# ---------- TODO:develop env only
#COPY deploy/debian/sources.list.txt /etc/apt/sources.list
#RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# ----------

COPY . /app
COPY ./pelican_publisher/pelican_publisher/settings/docker.py /app/pelican_publisher/pelican_publisher/settings/running.py

RUN apt-get update && apt-get install --yes supervisor redis-server
COPY deploy/supervisor/*.conf /etc/supervisor/conf.d/

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements-pelican.txt

WORKDIR /app/pelican_publisher
EXPOSE 8000

RUN mkdir /pelican-output
VOLUME /pelican-output

RUN ./manage.py migrate --no-input
#RUN ./manage.py collectstatic --no-input

# TODO: nobody
CMD ./docker-start-service.sh

#!/bin/zsh

docker pull python:3.14-alpine
docker build -t ray1ex/pelican-publisher . --build-arg ENV=rex

read -r -s -k '?Press any key to continue. startup container...'
docker container stop pelican-publisher
docker container rm pelican-publisher
docker run -dit -p 127.0.0.1:8000:8000 \
  -v /tmp:/output -v /tmp:/log \
  -e DEBUG=true \
  --name pelican-publisher ray1ex/pelican-publisher
docker container logs -f pelican-publisher
docker image prune -f
docker volume prune -f

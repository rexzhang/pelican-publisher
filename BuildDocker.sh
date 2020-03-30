docker container stop pelican-publisher
docker container rm pelican-publisher

#docker pull python:3
docker build -t ray1ex/pelican-publisher .
# shellcheck disable=SC2046
docker rmi -f $(docker images -qa -f "dangling=true")

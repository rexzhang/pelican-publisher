docker container stop pelican-publisher
docker container rm pelican-publisher
docker image rm pelican-publisher

docker build -t ray1ex/pelican-publisher .
# shellcheck disable=SC2046
docker rmi -f $(docker images -qa -f "dangling=true")

docker run -dit -p 127.0.0.1:8000:8000 -v /tmp:/pp-output -e DEBUG=true \
  --name pelican-publisher ray1ex/pelican-publisher
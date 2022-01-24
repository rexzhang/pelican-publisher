docker container stop pelican-publisher
docker container rm pelican-publisher
docker image rm ray1ex/pelican-publisher

docker build -t ray1ex/pelican-publisher .
docker image prune -f

docker run -dit -p 127.0.0.1:8000:8000 -v /tmp:/pp-output -e DEBUG=true \
  --name pelican-publisher ray1ex/pelican-publisher

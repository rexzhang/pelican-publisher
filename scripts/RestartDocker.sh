docker container stop pelican-publisher
docker container rm pelican-publisher

docker run -dit -p 127.0.0.1:8000:8000 --name pelican-publisher ray1ex/pelican-publisher

docker container stop pelican-publisher
docker container rm pelican-publisher

docker run -dit -p 127.0.0.1:8000:8000 -v=/Users/rex/TEMP/pelican-output:/pelican-output --env-file pelican-publisher.env --name pelican-publisher ray1ex/pelican-publisher
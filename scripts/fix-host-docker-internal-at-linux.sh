#!/usr/bin/env bash

# https://dev.to/bufferings/access-host-from-a-docker-container-4099
# https://github.com/bufferings/docker-access-host
# fix docker inside access linux host's service, eg:  postgresql/redis ...

HOST_DOMAIN="host.docker.internal"
ping -q -c1 "$HOST_DOMAIN" > /dev/null 2>&1
if [ $? -ne 0 ]; then
  HOST_IP=$(ip route | awk 'NR==1 {print $3}')
  echo -e "$HOST_IP\t$HOST_DOMAIN" >> /etc/hosts
fi

# Here is the original entry point.
curl -sS host.docker.internal:8888
cat /etc/hosts

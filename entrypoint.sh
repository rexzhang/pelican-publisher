#!/bin/sh

./manage.py migrate --no-input
./runserver.py -H 0.0.0.0

# for dev
if [ "$DEBUG" = "true" ]; then python; fi

#!/usr/bin/env python
# coding=utf-8


from os import getenv

from .release import *

ALLOWED_HOSTS.append('127.0.0.1')
PELICAN['OUTPUT_PATH'] = '/pelican-output'

# import setting from env
for k in ('OUTPUT_PATH', 'SOURCE_ZIP_URL', 'SITE_SECRET'):
    v = getenv('PELICAN_{}'.format(k))
    if v:
        PELICAN[k] = v

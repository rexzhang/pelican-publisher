#!/usr/bin/env python
# coding=utf-8


from os import getenv

from .release import *

PELICAN['PUBLISHER_OUTPUT_PATH'] = '/publisher-output'

# import setting from env

# update settings.ALLOWED_HOSTS
pelican_publisher_domain = getenv('PELICAN_PUBLISHER_DOMAIN', '')
if pelican_publisher_domain == '':
    # default allow any host domain
    pelican_publisher_domain = '*'

ALLOWED_HOSTS.append(pelican_publisher_domain)

# update settings.PELICAN
for k in ('SITE_NAME', 'SOURCE_ZIP_URL', 'SITE_SECRET'):
    v = getenv('PELICAN_{}'.format(k), '')
    if v != '':
        PELICAN[k] = v

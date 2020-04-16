#!/usr/bin/env python
# coding=utf-8


import json
from os import getenv

from .release import *

PELICAN_PUBLISHER['WORKING_ROOT'] = '/tmp/pp-working'
PELICAN_PUBLISHER['OUTPUT_ROOT'] = '/tmp/pp-output'
DATABASES['default']['NAME'] = '/pp-data/db.sqlite3'

# import setting from env

# update settings.ALLOWED_HOSTS
pelican_publisher_domain = getenv('PELICAN_PUBLISHER_DOMAIN', '')
if pelican_publisher_domain == '':
    # default allow any host domain
    pelican_publisher_domain = '*'

ALLOWED_HOSTS.append(pelican_publisher_domain)

# update settings.PELICAN_SITE_SOURCES
pelican_site_sources_json_str = getenv('PELICAN_SITE_SOURCES', '')
if pelican_site_sources_json_str != '':
    try:
        pelican_site_sources = json.loads(pelican_site_sources_json_str)
        for pelican_site_source in pelican_site_sources:
            if set(pelican_site_source.keys()) < {'NAME', 'ZIP_URL', 'SECRET'}:
                raise ValueError

        PELICAN_SITE_SOURCES = pelican_site_sources

    except ValueError:
        raise Exception('env PELICAN_SITE_SOURCES incorrect')

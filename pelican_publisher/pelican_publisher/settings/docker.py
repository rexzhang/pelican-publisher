#!/usr/bin/env python
# coding=utf-8


import json
from os import getenv
from logging import getLogger

from .release import *

logger = getLogger(__name__)

PELICAN_PUBLISHER['OUTPUT_ROOT'] = '/pp-output'
DATABASES['default']['NAME'] = '/pp-data/db.sqlite3'

# import setting from env

# update settings.ALLOWED_HOSTS
pelican_publisher_domain = getenv('PELICAN_PUBLISHER_DOMAIN', '')
if pelican_publisher_domain == '':
    # default allow any host domain
    pelican_publisher_domain = '*'

ALLOWED_HOSTS.append(pelican_publisher_domain)
logger.info('ALLOWED_HOSTS: {}'.format(ALLOWED_HOSTS))

# update settings.PELICAN_SITES
pelican_sites_json_str = getenv('PELICAN_SITES', '')
if pelican_sites_json_str != '':
    try:
        pelican_sites = json.loads(pelican_sites_json_str)
        for pelican_site_info in pelican_sites:
            if set(pelican_site_info.keys()) < {'NAME', 'ZIP_URL', 'WEBHOOK_SECRET'}:
                raise ValueError

        PELICAN_SITES = pelican_sites
        logger.info('env PELICAN_SITES import')

    except ValueError:
        logger.critical('env PELICAN_SITES incorrect')
        raise Exception('env PELICAN_SITES incorrect')

#!/usr/bin/env python
# coding=utf-8


import subprocess
from logging import getLogger
from pathlib import PurePath, Path
from shutil import rmtree
from uuid import uuid4
from zipfile import ZipFile

import requests
from django.conf import settings

logger = getLogger(__name__)


def build_pelican_site():
    site_stage_path, site_file_path = download_and_extract_zip_from_github()
    if site_file_path is None:
        return

    content_path = PurePath(site_file_path).joinpath('content')
    settings_file = PurePath(site_file_path).joinpath('pelicanconf.py')
    output_path = settings.PELICAN['OUTPUT_PATH']

    generate_site_to_local_file(
        content_path=content_path, settings_file=settings_file, output_path=output_path
    )

    # cleanup
    rmtree(site_stage_path, ignore_errors=True)
    return


def download_and_extract_zip_from_github():
    """
    from https://pelican-blog/archive/master.zip
    to: /path/pelican-blog
    """
    tmp_name = 'p-{}-{}'.format(settings.PELICAN['SITE_NAME'], uuid4().hex)
    zip_file_url = settings.PELICAN['SITE_SOURCE_ZIP_URL']
    zip_file_name = PurePath('/tmp').joinpath('{}-branch.zip'.format(tmp_name)).as_posix()
    site_stage_path = PurePath('/tmp').joinpath('{}-stage'.format(tmp_name))
    logger.debug('zip file name: {}'.format(zip_file_name))

    # download zip file
    r = requests.get(zip_file_url)
    if not r.ok:
        logger.error('download failed')
        return None, None

    open(zip_file_name, 'wb').write(r.content)
    logger.info('download finished')

    # extract zip file
    ZipFile(zip_file_name).extractall(site_stage_path)

    # pelican site file check
    site_file_path = None
    for p in Path(site_stage_path).glob('*'):
        if p.is_dir():
            site_file_path = p.as_posix()
            break

    if site_file_path is None:
        logger.error('pelican site file extract failed, more subdir')
        return None, None

    logger.info('extracted pelican site file to: {}'.format(site_file_path))
    return site_stage_path, site_file_path


def generate_site_to_local_file(content_path, settings_file, output_path):
    subprocess.run(
        ['pelican', '-s', settings_file, '-o', output_path, content_path]
    )
    logger.info('build to: {} finished'.format(output_path))
    return

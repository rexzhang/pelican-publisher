#!/usr/bin/env python
# coding=utf-8


import subprocess

from django.conf import settings
from celery import shared_task


@shared_task(rate_limit='1/m')
def demo_task():
    print('demo task')


def download_repos():
    """
    from git:pelican-blog.git
    to: /path/pelican-blog
    """
    return


def generate_site():
    output_path = settings.PELICAN_OUTPUT_PATH
    subprocess.run(
        ['pelican', '-o', output_path]
    )
    return

#!/usr/bin/env python
# coding=utf-8


from celery import shared_task

from . import runtimes


@shared_task(rate_limit='1/m')
def builder_pelican_site():
    runtimes.builder_pelican_site()
    return

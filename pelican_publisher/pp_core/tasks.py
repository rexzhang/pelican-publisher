#!/usr/bin/env python
# coding=utf-8


from celery import shared_task

from . import runtimes


@shared_task(rate_limit='1/m')
def build_pelican_site(site_name, request_time):
    runtimes.build_pelican_site()
    return

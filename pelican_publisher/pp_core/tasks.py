#!/usr/bin/env python
# coding=utf-8


from celery import shared_task

from .runtimes.build_pelican_site import build_pelican_site


@shared_task
def test_task(arg1, arg2):
    return {
        'a': 'aaaaaa',
        'b': 2222,
    }


@shared_task(rate_limit='1/m')
def build_pelican_site(site_name, request_time):
    build_pelican_site()
    return

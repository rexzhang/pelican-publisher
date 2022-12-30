#!/usr/bin/env python


from celery import shared_task

from .runtimes.build_pelican_site import build_pelican_site, test


@shared_task
def test_task(arg1, arg2):
    return test(arg1, arg2)


@shared_task(rate_limit="1/m")
def build_pelican_site_task(site_name, request_time):
    return build_pelican_site(site_name)

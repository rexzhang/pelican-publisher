#!/usr/bin/env python
# coding=utf-8


from typing import Union

from django.conf import settings


def get_site_info_by_name(site_name) -> Union[dict, None]:
    for site_info in settings.PELICAN_SITE_SOURCES:
        if site_info['NAME'] == site_name:
            return site_info

    return None

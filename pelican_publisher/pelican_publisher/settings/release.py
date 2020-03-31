#!/usr/bin/env python
# coding=utf-8


"""
Eve Map Online 项目"发布环境"基础设置文件
"""

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .base import *

#
# Security
#
DEBUG = False
ALLOWED_HOSTS = ['pelican-publisher.rexzhang.com']

#
# Sentry
#
sentry_sdk.init(
    dsn="https://f91e39ed295d40ef9ca267abbd4b4c40@sentry.io/5182540",
    environment='release',

    integrations=[DjangoIntegration(), RedisIntegration(), CeleryIntegration(), LoggingIntegration()]
)

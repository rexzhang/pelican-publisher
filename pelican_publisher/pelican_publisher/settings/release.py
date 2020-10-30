#!/usr/bin/env python
# coding=utf-8


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .base import *  # noqa: F401, F403

#
# Security
#
DEBUG = False
ALLOWED_HOSTS = []

#
# Sentry
#
sentry_sdk.init(
    dsn="https://f91e39ed295d40ef9ca267abbd4b4c40@sentry.io/5182540",
    environment='release',

    integrations=[
        DjangoIntegration(), RedisIntegration(), CeleryIntegration(),
        LoggingIntegration()
    ],

    # be sure to lower this in production to prevent quota issues
    traces_sample_rate=1.0,
)

from os import getenv

from pelican_publisher import __version__
from pelican_publisher.sentry import init_sentry

from .base import *  # noqa: F401, F403

#
# Security
#
DEBUG = False
ALLOWED_HOSTS = []

#
# Sentry
#
SENTRY_DSN = getenv("SENTRY_DSN", "")
if SENTRY_DSN:
    from sentry_sdk.integrations.asyncio import AsyncioIntegration
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    init_sentry(
        dsn=SENTRY_DSN,
        integrations=[AsyncioIntegration(), DjangoIntegration(), LoggingIntegration()],
        app_name="PelicanPublisher",
        app_version=__version__,
        user_id_is_mac_address=True,
    )

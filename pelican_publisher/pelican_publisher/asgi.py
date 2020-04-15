"""
ASGI config for pelican_publisher project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.core.asgi import get_asgi_application
from asgi_middleware_static_file import ASGIMiddlewareStaticFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pelican_publisher.settings')

application = get_asgi_application()
application = ASGIMiddlewareStaticFile(
    application, static_url=settings.STATIC_URL, static_paths=[settings.STATIC_ROOT]
)

#!/usr/bin/env python


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ("celery_app", "__version__")

__name__ = "Pelican Publisher"
__version__ = "0.4.2"

__project_url__ = "https://github.com/rexzhang/pelican-publisher"
__docker_url__ = "https://hub.docker.com/r/ray1ex/pelican-publisher"

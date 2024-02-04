from logging import getLogger

from .release import *  # noqa F403

logger = getLogger(__name__)


if len(ALLOWED_HOSTS) == 0:  # noqa F405
    # default allow any host domain
    ALLOWED_HOSTS.append("*")  # noqa F405

PELICAN_PUBLISHER["OUTPUT_ROOT"] = "/output"  # noqa F405
DATABASES["default"]["NAME"] = "/data/db.sqlite3"  # noqa F405

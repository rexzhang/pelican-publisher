from django.conf import settings

from pelican_publisher.settings import PelicanSite


def get_pelican_site_by_name(site_name: str) -> PelicanSite | None:
    for pelican_site in settings.PELICAN_SITES:
        if pelican_site.NAME == site_name:
            return pelican_site

    return None

from django.conf import settings


def get_site_info_by_name(site_name) -> dict | None:
    for site_info in settings.PELICAN_SITES:
        if site_info["NAME"] == site_name:
            return site_info

    return None

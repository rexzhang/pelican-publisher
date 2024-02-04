from django_toosimple_q.decorators import register_task

from .runtimes.build_pelican_site import build_pelican_site, test


@register_task()
def test_task(arg1, arg2):
    return test(arg1, arg2)


@register_task(retries=3, retry_delay=3)
def build_pelican_site_task(site_name):
    return build_pelican_site(site_name)

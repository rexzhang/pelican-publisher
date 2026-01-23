from django_tasks import task

from .runtimes.build_pelican_site import build_pelican_site, test


@task()
def test_task(arg1, arg2):
    return test(arg1, arg2)


@task()
def build_pelican_site_task(site_name):
    return build_pelican_site(site_name)

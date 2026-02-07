from collections.abc import Callable
from datetime import datetime

from django.tasks import task

from .constans import ShelRunResponse, TaskStatus
from .models import Task
from .runtimes.build_pelican_site import build_pelican_site, test


def _exec_shell_task(func: Callable, site_name: str):
    task = Task(
        site_name=site_name, status=TaskStatus.RUNNING.value, started_at=datetime.now()
    )
    task.save()

    try:
        shell_run_response: ShelRunResponse = func(site_name)
    except Exception as e:
        shell_run_response = ShelRunResponse(999, "", f"{e}")

    if shell_run_response.returncode == 0:
        task.status = TaskStatus.SUCCESSFUL.value
    else:
        task.status = TaskStatus.FAILED.value

    task.finished_at = datetime.now()
    task.stdout = shell_run_response.stdout
    task.stderr = shell_run_response.stderr
    task.save()


@task()
def test_task(site_name: str):
    return _exec_shell_task(test, site_name)


@task()
def build_pelican_site_task(site_name: str):
    return _exec_shell_task(build_pelican_site, site_name)

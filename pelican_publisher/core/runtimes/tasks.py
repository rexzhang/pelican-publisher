from django.db.models import QuerySet
from django_tasks import TaskResultStatus
from django_tasks.backends.database.models import DBTaskResult

task_states_pending = {TaskResultStatus.READY, TaskResultStatus.RUNNING}
task_states_end = {TaskResultStatus.SUCCEEDED, TaskResultStatus.FAILED}


def get_pending_task_query_set() -> QuerySet:
    return DBTaskResult.objects.filter(status__in=task_states_pending).order_by(
        "-enqueued_at"
    )


def get_finished_task_query_set(bumber: int = 10) -> QuerySet:
    return DBTaskResult.objects.filter(status__in=task_states_end).order_by(
        "-finished_at"
    )

from django_tasks import TaskResult, TaskResultStatus
from django_tasks.backends.database.models import DBTaskResult

task_states_pending = {TaskResultStatus.READY, TaskResultStatus.RUNNING}
task_states_finished = {TaskResultStatus.SUCCEEDED, TaskResultStatus.FAILED}


def get_pending_task_list() -> list[TaskResult]:
    return [
        task.task_result
        for task in DBTaskResult.objects.filter(
            status__in=task_states_pending
        ).order_by("-enqueued_at")
    ]


def get_end_task_list(number: int = 10) -> list[TaskResult]:
    return [
        task.task_result
        for task in DBTaskResult.objects.filter(
            status__in=task_states_finished
        ).order_by("-finished_at")[:number]
    ]

from django_toosimple_q.models import TaskExec, WorkerStatus

pending_states = [
    TaskExec.States.SLEEPING,
    TaskExec.States.QUEUED,
    TaskExec.States.PROCESSING,
]


def get_pending_task_list() -> list:
    return TaskExec.objects.filter(state__in=pending_states).order_by("-created")


def get_finished_task_list(bumber: int = 10) -> list:
    return TaskExec.objects.exclude(state__in=pending_states).order_by("-finished")[:10]

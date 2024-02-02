from django_toosimple_q.models import TaskExec, WorkerStatus

pending_states = [
    TaskExec.States.SLEEPING,
    TaskExec.States.QUEUED,
    TaskExec.States.PROCESSING,
]


def get_pending_task_list() -> list:
    return TaskExec.objects.filter(state__in=pending_states).all()


def get_finished_task_list(bumber: int = 10) -> list:
    return TaskExec.objects.exclude(state__in=pending_states)[:10]

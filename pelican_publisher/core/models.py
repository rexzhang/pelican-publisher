from django.db import models
from django_vises.db.model.base import RecordAbc

from .constans import TaskStatus


class Task(RecordAbc):
    site_name = models.CharField()
    status = models.CharField(default=TaskStatus.READY.value)

    stdout = models.TextField(null=True)
    stderr = models.TextField(null=True)

    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)

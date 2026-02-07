from dataclasses import dataclass
from enum import auto

from django_vises.common.enum import EnumUpperAbc


class TaskStatus(EnumUpperAbc):
    READY = auto()
    RUNNING = auto()
    FAILED = auto()
    SUCCESSFUL = auto()


@dataclass
class ShelRunResponse:
    returncode: int
    stdout: str
    stderr: str

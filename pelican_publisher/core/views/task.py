from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView as DjangoDetailView
from django.views.generic import TemplateView as DjangoTemplateView

import pelican_publisher
from pelican_publisher.core.constans import TaskStatus
from pelican_publisher.core.models import Task
from pelican_publisher.core.tasks import test_task


class ViewMixin:
    @staticmethod
    def _update_context_data(context: dict):
        context.update(
            {
                "app_name": pelican_publisher.__name__,
                "app_version": pelican_publisher.__version__,
                "app_project_url": pelican_publisher.__project_url__,
                "app_docker_url": pelican_publisher.__docker_url__,
            }
        )


class TemplateView(ViewMixin, DjangoTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self._update_context_data(context)

        return context


class DetailView(ViewMixin, DjangoDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self._update_context_data(context)

        return context


class CallTestView(TemplateView):
    template_name = "pp_core/task/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        test_task.enqueue("example.com")
        return context


class HomeView(TemplateView):
    template_name = "pp_core/task/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "pending_task_list": Task.objects.filter(
                    status__in=[TaskStatus.READY.value, TaskStatus.RUNNING.value]
                )
                .order_by("-created_time")
                .all(),
                "finished_task_list": Task.objects.filter(
                    status__in=[TaskStatus.FAILED.value, TaskStatus.SUCCESSFUL.value]
                ).order_by("-created_time")[:10],
            }
        )
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "pp_core/task/detail.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = self.model.objects.filter(id=pk).first()
        if obj is None:
            raise ObjectDoesNotExist("incorrect task id")

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

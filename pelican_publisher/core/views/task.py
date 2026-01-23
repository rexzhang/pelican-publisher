from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView as DjangoDetailView
from django.views.generic import TemplateView as DjangoTemplateView
from django_tasks.backends.database.models import DBTaskResult

import pelican_publisher
from pelican_publisher.core.runtimes.tasks import (
    get_end_task_list,
    get_pending_task_list,
)
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


class TestView(TemplateView):
    template_name = "pp_core/task/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        test_task.enqueue(1, 2)
        return context


class HomeView(TemplateView):
    template_name = "pp_core/task/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "pending_task_list": get_pending_task_list(),
                "finished_task_list": get_end_task_list(),
            }
        )
        return context


class TaskDetailView(DetailView):
    model = DBTaskResult
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

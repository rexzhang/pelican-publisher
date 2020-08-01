#!/usr/bin/env python
# coding=utf-8


import json

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView as DjangoTemplateView, DetailView as DjangoDetailView
from django_celery_results.models import TaskResult

import pelican_publisher
from .runtimes.celery import get_pending_task_list
from .tasks import test_task


class TemplateView(DjangoTemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = pelican_publisher.__version__

        return context


class DetailView(DjangoDetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = pelican_publisher.__version__

        return context


class TestView(TemplateView):
    template_name = 'pp_core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        test_task.delay(1, 2)
        return context


class HomeView(TemplateView):
    template_name = 'pp_core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pending_list'] = get_pending_task_list()
        context['task_result_list'] = TaskResult.objects.all()[:10]
        return context


class TaskResultDetailView(DetailView):
    model = TaskResult
    template_name = 'pp_core/task_result_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = self.model.objects.filter(task_id=pk).first()
        if obj is None:
            raise ObjectDoesNotExist('incorrect task id')

        obj.result = json.loads(obj.result)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

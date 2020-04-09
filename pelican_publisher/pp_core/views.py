#!/usr/bin/env python
# coding=utf-8


from django.views.generic import TemplateView

from .runtimes.celery import get_pending_task_list


class HomeView(TemplateView):
    template_name = "pp_core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_list'] = get_pending_task_list()
        return context

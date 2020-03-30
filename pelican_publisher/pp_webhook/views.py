#!/usr/bin/env python
# coding=utf-8


from django.views.generic import TemplateView

from .tasks import demo_task


class GithubPushView(TemplateView):
    template_name = "webhook/github_push.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = 'aaaaa'

        demo_task.delay()
        return context

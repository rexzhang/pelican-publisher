#!/usr/bin/env python
# coding=utf-8


from django.views.generic import TemplateView

from pp_core.tasks import builder_pelican_site


class GithubPushView(TemplateView):
    template_name = "webhook/github_push.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = 'aaaaa'

        builder_pelican_site.delay()
        return context

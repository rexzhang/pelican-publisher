#!/usr/bin/env python
# coding=utf-8


from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pp_core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

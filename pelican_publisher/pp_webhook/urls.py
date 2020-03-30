#!/usr/bin/env python
# coding=utf-8


from django.urls import path

from .views import GithubPushView

urlpatterns = [
    path('github-push', view=GithubPushView.as_view(), name='github-push'),
]

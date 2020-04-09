#!/usr/bin/env python
# coding=utf-8


from django.urls import path

from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('github', view=views.github_webhook, name='github'),
]

#!/usr/bin/env python


from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path("github/<str:site_name>", view=views.github_webhook, name="github"),
]

if settings.DEBUG:
    urlpatterns.append(
        path("test", views.test, name="test"),
    )

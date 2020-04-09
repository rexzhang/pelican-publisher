#!/usr/bin/env python
# coding=utf-8


"""pelican_publisher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from pp_core.views import HomeView, TaskResultDetailView

urlpatterns = [
    path('', view=HomeView.as_view(), name='home'),
    path('<pk>/', TaskResultDetailView.as_view(), name='task-result-detail'),
    path('webhook/', include(('pp_webhook.urls', 'pp_webhook'), namespace='pp-webhook')),
]

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

from django.conf import settings
from django.urls import include, path

from pp_core.views import task, web_hook

urlpatterns = [
    path("", view=task.HomeView.as_view(), name="home"),
    path(
        "task/<int:pk>/",
        task.TaskDetailView.as_view(),
        name="task-detail",
    ),
    path(
        "webhook/github/<str:site_name>",
        view=web_hook.github_webhook,
        name="web-hook-github",
    ),
]

if settings.DEBUG:
    # from django.contrib import admin
    urlpatterns += [
        # path("admin/", admin.site.urls),
        path("__reload__/", include("django_browser_reload.urls")),
        path("task/test", view=task.TestView.as_view(), name="task-test"),
        path("webhook/test", web_hook.test, name="web-hook-test"),
    ]

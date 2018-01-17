from django.conf.urls import url
from django.contrib import admin

app_name = "accunts"

from .views import (
    UserCreateAPIView,
    TasksListForUserView
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^metasks/$', TasksListForUserView.as_view(),name='metasks'),
    ]

from django.conf.urls import url
from django.contrib import admin

app_name = "accunts"

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserView
    )

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^user/',UserView.as_view()),
]

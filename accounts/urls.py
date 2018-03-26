from django.conf.urls import url
from django.contrib import admin

app_name = "accunts"

from .views import (
    UserCreateAPIView,
    TasksListForUserView,
    ProfileUserView,
    MeetingListForUserView,
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^mytasks/$', TasksListForUserView.as_view(),name='mytasks'),
    url(r'^myprofile/$', ProfileUserView.as_view(),name='meprofile'),
    url(r'^mymeetings/$', MeetingListForUserView.as_view(),name='mymeetings'),
    ]

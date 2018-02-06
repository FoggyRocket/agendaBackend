from django.shortcuts import render
from .models import Meeting
#api
from rest_framework import viewsets
from .serializers import MeetingSerializer

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer

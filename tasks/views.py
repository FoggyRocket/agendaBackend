from django.shortcuts import render
from .models import Task
#api
from rest_framework import viewsets
from .serializers import TasksSerializer

# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TasksSerializer

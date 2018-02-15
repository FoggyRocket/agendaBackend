from django.shortcuts import render
from .models import Task
#api
from rest_framework import viewsets
from .serializers import TasksSerializer, BasicTasksSerializer

# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TasksSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return TasksSerializer
		if self.action == 'retrive':
			return BasicTasksSerializer
		return BasicTasksSerializer

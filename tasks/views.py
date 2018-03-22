from django.shortcuts import render
from .models import Task
#api
from rest_framework import viewsets
from .serializers import TasksSerializer, EditTasksSerializer

# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TasksSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditTasksSerializer
		if self.action == 'partial_update':
			return EditTasksSerializer
		return TasksSerializer

from django.shortcuts import render
from .models import Project
# api
from rest_framework import viewsets
from .serializers import ProjectSerializer, EditProjectSerializer


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return EditProjectSerializer
        if self.action == 'partial_update':
            return EditProjectSerializer
        return ProjectSerializer

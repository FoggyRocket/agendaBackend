from django.shortcuts import render
from .models import Project
# api
from rest_framework import viewsets
from .serializers import ProjectSerializer, EditProjectSerializer, BasicProjectSerializer
from .models import Project
from rest_framework.response import Response


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    #model = Project
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action =='update':
            return EditProjectSerializer
        if self.action == 'partial_update':
            return EditProjectSerializer
        return ProjectSerializer

    # Determina el queryset que debe crear
    # def get_queryset(self):
    #     # Recupera el usuario que hace la petición
    #     user = self.request.user
    #     # Crea el queryset
    #     # Filtra y recupera solo los proyectos que pertenecen al usuario
    #     return Project.objects.filter(user=user)
    #
    # def get_serializer_class(self):
    #     if self.action == 'update':
    #         return EditProjectSerializer
    #     if self.action == 'partial_update':
    #         return EditProjectSerializer
    #     if self.action == 'retrieve' or self.action == 'list':
    #         return ProjectSerializer
    #     return BasicProjectSerializer
    #
    #
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

from rest_framework import serializers
from .models import Project
from tasks.serializers import TasksSerializer, UserSerializer
from tasks.models import Task

"""
class BasicProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all___'
"""


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True, allow_null=True)
    tasks_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Task.objects.all(), allow_null=True)
    user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        tasks = validated_data.pop('tasks_ids')
        project = Project.objects.create(**validated_data)
        for task in tasks:
            project.tasks.add(task)

        return project


class EditProjectSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True)
    tasks_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Task.objects.all(),
                                                   source="tasks")
    user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = '__all__'

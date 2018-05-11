from rest_framework import serializers
from .models import Project
from accounts.models import Profile
from tasks.serializers import TasksSerializer, UserSerializer
from tasks.models import Task
from meeting.serializers import ProfileSerializer

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
    participants = ProfileSerializer(many=True, read_only=True, allow_null=True)
    participants_id=serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Profile.objects.all(),allow_null = True)
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        tasks = validated_data.pop('tasks_ids')
        participants=validated_data.pop('participants_id')
        project = Project.objects.create(**validated_data)
        for task in tasks:
            project.tasks.add(task)
        for p in participants:
            project.participants.add(p)
        return project


class EditProjectSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True)
    tasks_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Task.objects.all(),
                                                   source="tasks")
    user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
    participants = ProfileSerializer(many=True, read_only=True)
    participants_id=serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Profile.objects.all(), source="participants")
    class Meta:
        model = Project
        fields = '__all__'


class BasicProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= '__all__'

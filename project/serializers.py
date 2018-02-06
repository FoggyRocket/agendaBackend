from rest_framework import serializers
from .models import Project
from meeting.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ['name', 'id']


class ProjectSerializer(serializers.ModelSerializer):
	meeting = MeetingSerializer(many=False, read_only=True)
	class Meta:
		model = Meeting
		fields = '__all__'

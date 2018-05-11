from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from accounts.models import Profile
from meeting.models import Meeting
from project.models import Project


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id']

class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ['id', 'name']
class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model= Project
		fields= ['id','name_project']


class EditTasksSerializer(serializers.ModelSerializer):
	meeting = MeetingSerializer(many=False, read_only=True,allow_null = True)
	user = UserSerializer(many=False, read_only=True,allow_null = True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(), source="meeting",allow_null=True)
	user_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=User.objects.all(),source="user",allow_null=True)
	project = ProjectSerializer(many=False, read_only=True, allow_null=True)
	project_id = serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Project.objects.all(),source="project",allow_null=True)
	class Meta:
		model = Task
		fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
	meeting = MeetingSerializer(many=False, read_only=True,allow_null = True)
	user = UserSerializer(many=False, read_only=True,allow_null = True,)
	project = ProjectSerializer(many=False, read_only=True,allow_null=True)
	project_id = serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Project.objects.all(),allow_null=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(),allow_null=True)
	user_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=User.objects.all(),allow_null = True)
	class Meta:
		model = Task
		fields = '__all__'
	def create(self,validated_data):
		print(validated_data)
		meeting=validated_data.pop('meeting_id')
		user=validated_data.pop('user_id')
		project=validated_data.pop('project_id')
		task= Task.objects.create(meeting=meeting,user=user,project=project,**validated_data)

		return task

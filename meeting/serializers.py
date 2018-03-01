from rest_framework import serializers
from .models import Meeting,Files,Action,Note
from django.contrib.auth.models import User
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id']

class ProfileSerializer(serializers.ModelSerializer):
	user= UserSerializer(many=False, read_only=True)
	class Meta:
		model = Profile
		fields = ['id','avatar','user']

class MeetingSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
	participants = ProfileSerializer(many=True, read_only=True)
	class Meta:
		model = Meeting
		fields = '__all__'

class BasicMeetinSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ['name', 'id']

class FileSerializer(serializers.ModelSerializer):
	meeting = BasicMeetinSerializer(many=False, read_only=True)
	class Meta:
		model = Files
		fields = '__all__'
class BasicFilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Files
		fields = '__all__'

class BasicActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Action
		fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
	meeting = BasicMeetinSerializer(many=False, read_only=True)
	class Meta:
		model = Action
		fields = '__all__'

class BasicNoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
	meeting = BasicMeetinSerializer(many=False, read_only=True)
	autor = ProfileSerializer(many=False, read_only=True)
	class Meta:
		model = Note
		fields = '__all__'

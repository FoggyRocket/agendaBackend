from rest_framework import serializers
from .models import Meeting,Files,Order,Note, Action
from django.contrib.auth.models import User
from accounts.models import Profile
from tasks.models import Task



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['username', 'id']

class ProfileSerializer(serializers.ModelSerializer):
	user= UserSerializer(many=False, read_only=True)

	class Meta:
		model = Profile
		fields = ['id','avatar','user']

"basic serializers"

class BasicTasksSerializer(serializers.ModelSerializer):
	user= UserSerializer(many=False, read_only=True)
	class Meta:
		model = Task
		fields = '__all__'
class BasicNoteSerializer(serializers.ModelSerializer):
	autor=ProfileSerializer(many=False,read_only=True)
	class Meta:
		model= Note
		fields = ["id","autor","text","created"]

class BasicOrderSerializer(serializers.ModelSerializer):
	class Meta:
		model= Order
		fields = ["id","name_order","created","status"]
class BasicActionSerializer(serializers.ModelSerializer):
	user=UserSerializer(many=False,read_only=True)
	class Meta:
		model=Action
		fields =["id","user","text","created"]

class BasicFileSerializer(serializers.ModelSerializer):
	class Meta:
		model=Files
		fields = "__all__"

class BasicMeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ['name', 'id']






class FileSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all())

	class Meta:
		model = Files
		fields = '__all__'

	def create(self,validated_data):
		print(validated_data)
		meeting=validated_data.pop('meeting_id')
		files= Files.objects.create	(meeting=meeting,**validated_data)

		return files

class EditFilesSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(),source="meeting")
	class Meta:
		model = Files
		fields = '__all__'

class EditOrderSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(),source="meeting")
	class Meta:
		model = Order
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all())
	class Meta:
		model = Order
		fields = '__all__'
	def create(self,validated_data):
		print(validated_data)
		meeting=validated_data.pop('meeting_id')
		order= Order.objects.create(meeting=meeting,**validated_data)

		return order

class EditNoteSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(),source="meeting")
	class Meta:
		model = Note
		fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	autor = ProfileSerializer(many=False, read_only=True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all())
	autor_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Profile.objects.all())
	class Meta:
		model = Note
		fields = '__all__'

	def create(self,validated_data):
		print(validated_data)
		meeting=validated_data.pop('meeting_id')
		autor=validated_data.pop('autor_id')
		note= Note.objects.create(meeting=meeting,autor=autor,**validated_data)

		return note


class EditActionSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	user = UserSerializer(many=False, read_only=True,allow_null = True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all(), source="meeting")
	user_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=User.objects.all(),source="user",allow_null = True)
	class Meta:
		model = Action
		fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
	meeting = BasicMeetingSerializer(many=False, read_only=True)
	user = UserSerializer(many=False, read_only=True,allow_null = True)
	meeting_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=Meeting.objects.all())
	user_id=serializers.PrimaryKeyRelatedField(many=False,write_only=True, queryset=User.objects.all(),allow_null = True)
	class Meta:
		model = Action
		fields = '__all__'
	def create(self,validated_data):
		print(validated_data)
		meeting=validated_data.pop('meeting_id')
		user=validated_data.pop('user_id')
		action= Action.objects.create(meeting=meeting,user=user,**validated_data)

		return action

class MeetingSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
	participants = ProfileSerializer(many=True, read_only=True, allow_null=True)
	participants_id=serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Profile.objects.all(),allow_null = True)
	tasks=BasicTasksSerializer(many=True, read_only=True)
	notes=BasicNoteSerializer(many=True, read_only=True)
	order=BasicOrderSerializer(many=True, read_only=True)
	files=FileSerializer(many=True, read_only=True)
	action=BasicActionSerializer(many=True, read_only=True)

	class Meta:
		model = Meeting
		fields = '__all__'

	def create(self,validated_data):
		print(validated_data)
		participants=validated_data.pop('participants_id')
		meeting= Meeting.objects.create(**validated_data)
		for p in participants:
			meeting.participants.add(p)
		return meeting

class EditMeetingSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True, default=serializers.CurrentUserDefault())
	participants = ProfileSerializer(many=True, read_only=True)
	participants_id=serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Profile.objects.all(), source="participants")

	class Meta:
		model = Meeting
		fields = '__all__'

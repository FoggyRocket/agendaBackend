from django.shortcuts import render
from .models import Meeting, Files, Action, Note
#api
from rest_framework import viewsets
from .serializers import MeetingSerializer,FileSerializer,BasicFilesSerializer, BasicActionSerializer, ActionSerializer, BasicNoteSerializer, NoteSerializer

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer


class FileViewSet(viewsets.ModelViewSet):
	queryset = Files.objects.all()
	serializer_class = FileSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return FileSerializer
		if self.action == 'retrive':
			return BasicFilesSerializer
		return BasicFilesSerializer

class ActionViewSet(viewsets.ModelViewSet):
	queryset = Action.objects.all()
	serializer_class = ActionSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return ActionSerializer
		if self.action == 'retrive':
			return ActionSerializer
		return BasicActionSerializer

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return NoteSerializer
		if self.action == 'retrive':
			return NoteSerializer
		return BasicNoteSerializer

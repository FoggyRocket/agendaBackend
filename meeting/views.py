from django.shortcuts import render
from .models import Meeting, Files, Order, Note, Action
#api
from rest_framework import viewsets
from .serializers import  EditMeetingSerializer,MeetingSerializer,FileSerializer,BasicFilesSerializer, BasicOrderSerializer, OrderSerializer, BasicNoteSerializer, NoteSerializer, BasicActionSerializer,ActionSerializer

# Create your views here.
class MeetingViewSet(viewsets.ModelViewSet):
	queryset = Meeting.objects.all()
	serializer_class = MeetingSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditMeetingSerializer
		if self.action == 'partial_update':
			return EditMeetingSerializer
		return MeetingSerializer


class FileViewSet(viewsets.ModelViewSet):
	queryset = Files.objects.all()
	serializer_class = FileSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return FileSerializer
		if self.action == 'retrive':
			return BasicFilesSerializer
		return BasicFilesSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return OrderSerializer
		if self.action == 'retrive':
			return OrderSerializer
		return BasicOrderSerializer

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return NoteSerializer
		if self.action == 'retrive':
			return NoteSerializer
		return BasicNoteSerializer

class ActionViewSet(viewsets.ModelViewSet):
	queryset = Action.objects.all()
	serializer_class = ActionSerializer

	def get_serializer_class(self):
		if self.action == 'list':
			return ActionSerializer
		if self.action == 'retrive':
			return ActionSerializer
		return BasicActionSerializer

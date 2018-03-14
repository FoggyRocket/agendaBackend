from django.shortcuts import render
from .models import Meeting, Files, Order, Note, Action
#api
from rest_framework import viewsets
from .serializers import  EditMeetingSerializer,MeetingSerializer,FileSerializer,EditFilesSerializer, EditOrderSerializer, OrderSerializer, EditNoteSerializer, NoteSerializer, EditActionSerializer,ActionSerializer

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
		if self.action == 'update':
			return EditFilesSerializer
		if self.action == 'partial_update':
			return EditFilesSerializer
		return FileSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditOrderSerializer
		if self.action == 'partial_update':
			return EditOrderSerializer
		return OrderSerializer

class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditNoteSerializer
		if self.action == 'partial_update':
			return EditNoteSerializer
		return NoteSerializer

class ActionViewSet(viewsets.ModelViewSet):
	queryset = Action.objects.all()
	serializer_class = ActionSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditActionSerializer
		if self.action == 'partial_update':
			return EditActionSerializer
		return ActionSerializer

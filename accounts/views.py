from django.shortcuts import render
from .models import Profile,FastNote
from tasks.models import Task

#api
from rest_framework import viewsets, mixins
from .serializers import ProfileSerializer,UserCreateSerializer, UserSerializer,FastNoteSerializer,EditFastNoteSerializer
from tasks.serializers import TasksSerializer
from meeting.serializers import MeetingSerializer
from meeting.models import Meeting
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions, views, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.conf import settings
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    GenericAPIView
    )


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):

	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer



#User register
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

#user ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class UserView(views.APIView):
    def get(self,request):
        user=request.user
        return Response(UserSerializer(user).data)


#Rest password
class PasswordResetView(GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK
        )
#Filtrado Tareas User
class TasksListForUserView(ListAPIView):
    serializer_class = TasksSerializer

    def get_queryset(self):
        user=self.request.user
        return Task.objects.filter(user=user)


#Filtro Juntas de usuario
class MeetingListForUserView(ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        user=self.request.user
        participant=Profile.objects.get(user=user)
        meetings = Meeting.objects.all()

        return Meeting.objects.filter(participants__id=participant.id)




#Profile
class ProfileUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile, created= Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, context={"request":request})
        return Response(serializer.data)
    def post(self, request):
        profile, created= Profile.objects.get_or_create(user=request.user)
        serializer= ProfileSerializer(profile)
        return Response(serializer.data)

"Fast note"
class FastNoteViewSet(viewsets.ModelViewSet):
	queryset = FastNote.objects.all()
	serializer_class = FastNoteSerializer

	def get_serializer_class(self):
		if self.action == 'update':
			return EditFastNoteSerializer
		if self.action == 'partial_update':
			return EditFastNoteSerializer
		return FastNoteSerializer

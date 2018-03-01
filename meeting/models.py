from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    meeting_date = models.DateTimeField(auto_now_add=False,db_index=True)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    user = models.ForeignKey(User, related_name='project',limit_choices_to={'is_staff': True}, on_delete='CASCADE', blank=True, null=True)
    participants = models.ManyToManyField(Profile, blank=True)
    def __str__(self):
        return self.name

class Files(models.Model):

    name_file = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    meeting = models.ForeignKey(Meeting, related_name='file', on_delete='CASCADE', blank=True, null=True)
    files=models.FileField( upload_to='files/', blank=True, null=True)
    def __str__(self):
        return self.name_file

class Action(models.Model):
    name_action = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    meeting = models.ForeignKey(Meeting,related_name="action",on_delete='CASCADE', blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name_action

class Note(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    meeting = models.ForeignKey(Meeting, related_name='note',on_delete='CASCADE')
    autor = models.ForeignKey(Profile, related_name='note', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.text

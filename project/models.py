from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting
# Create your models here.

class Project(models.Model):

    name_project = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    meeting = models.ForeignKey(Meeting, related_name='meeting', on_delete='CASCADE', blank=True, null=True)
    def __str__(self):
        return self.name_project

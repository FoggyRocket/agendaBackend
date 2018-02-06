from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    meeting_date = models.DateTimeField(auto_now_add=False,db_index=True)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    user = models.ForeignKey(User, related_name='project',limit_choices_to={'is_staff': True}, on_delete='CASCADE', blank=True, null=True)
    participants = models.ManyToManyField(Profile)
    def __str__(self):
        return self.name

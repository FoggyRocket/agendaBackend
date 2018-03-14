from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting
from datetime import date
# Create your models here.


class Project(models.Model):
    name_project = models.CharField(max_length=100)
    created_date = models.DateField(auto_now=False,auto_now_add=False, db_index=True, default=date.today)
    due_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='project', limit_choices_to={'is_staff': True},
                             on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name_project

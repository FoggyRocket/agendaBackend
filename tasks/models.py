from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting
from project.models import Project
from django.conf import settings
# Create your models here.

class Task(models.Model):
	STATUS=(
	('Activo','Activo'),
	('Cumplido','Cumplido'),
	('Vencido','Vencido')
	)
	PRIORITY=(
	('Q3','Q3'),
	('Q2','Q2'),
	('Q1','Q1')
	)
	title =models.CharField(max_length=100, blank=True,null=True)
	text = models.TextField(blank=True,null=True)
	end = models.DateTimeField(auto_now_add=False, db_index=True, blank=True,null=True)
	start = models.DateTimeField(auto_now_add=False,db_index=True, blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True,db_index=True)
	status = models.CharField(max_length=100, choices=STATUS, default='Activo')
	priority = models.CharField(max_length=100, choices=PRIORITY, blank=True)
	allDay = models.BooleanField(default=True)
	user = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, blank=True, null=True)
	project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE,blank=True, null=True)
	meeting = models.ForeignKey(Meeting, related_name='tasks', on_delete=models.CASCADE,blank=True, null=True)

	def __str__(self):
		return self.title

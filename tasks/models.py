from django.db import models
from django.contrib.auth.models import User
from meeting.models import Meeting
from project.models import Project
# Create your models here.

class Task(models.Model):
	STATUS=(
	('Activo','Activo'),
	('Cumplido','Cumplido'),
	('Vencido','Vencido')
	)
	PRIORITY=(
	('Alta','Alta'),
	('Media','Media'),
	('Baja','Baja')
	)
	name =models.CharField(max_length=100, blank=True,null=True)
	text = models.TextField()
	expiry = models.DateTimeField(auto_now_add=False, db_index=True)
	starts = models.DateTimeField(auto_now_add=False,db_index=True)
	created = models.DateTimeField(auto_now_add=True,db_index=True)
	status = models.CharField(max_length=100, choices=STATUS, default='Activo')
	priority = models.CharField(max_length=100, choices=PRIORITY)
	user = models.ForeignKey(User, related_name='tasks', on_delete='CASCADE', blank=True, null=True)
	name_project = models.ForeignKey(Project, related_name='tasks', on_delete='CASCADE',blank=True, null=True)
	name_meeting = models.ForeignKey(Meeting, related_name='tasks', on_delete='CASCADE',blank=True, null=True)

	def __str__(self):
		return self.text

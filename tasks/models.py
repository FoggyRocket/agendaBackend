from django.db import models
from django.contrib.auth.models import User
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
	text = models.TextField()
	expiry = models.DateTimeField(auto_now_add=False, db_index=True)
	starts = models.DateTimeField(auto_now_add=False,db_index=True)
	created = models.DateTimeField(auto_now=True,db_index=True)
	status = models.CharField(max_length=100, choices=STATUS, default='Activo')
	priority = models.CharField(max_length=100, choices=PRIORITY)
	user = models.ForeignKey(User, related_name='tasks', on_delete='CASCADE', blank=True, null=True)

	def __str__(self):
		return self.text

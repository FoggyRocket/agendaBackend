from django.db import models

# Create your models here.

class Task(models.Model):
	text = models.TextField()
	expiry = models.DateTimeField(auto_now_add=True)
	starts = models.DateTimeField(auto_now_add=True)
	created = models.DateTimeField(auto_now=True)


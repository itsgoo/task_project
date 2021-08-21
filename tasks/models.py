from django.db import models

from .utils import status_types


class Task(models.Model):		
	creator = models.CharField(max_length=30, name='creator')
	email = models.EmailField(max_length=30, name='email')
	title = models.CharField(max_length=100, name='title')
	text = models.TextField(max_length=400, name='text')
	status = models.IntegerField(choices=status_types, verbose_name='status')
	edited_by_admin = models.BooleanField(default=False)

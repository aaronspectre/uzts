from django.db import models
from django.conf import settings


class Event(models.Model):
	title = models.CharField(max_length = 255)
	content = models.TextField()
	date = models.DateTimeField(auto_now = True)
	preview = models.ImageField(upload_to = 'static/img')
	announcement = models.BooleanField(default = False)

	def __str__(self):
		return self.title
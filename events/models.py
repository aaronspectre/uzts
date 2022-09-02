from django.db import models
from django.conf import settings



class ContentImage(models.Model):
	image = models.ImageField(upload_to = 'static/blog')

	def __str__(self):
		return self.image.name



class Content(models.Model):
	sequence = models.JSONField(default = list)
	titles = models.JSONField(default = list)
	plains = models.JSONField(default = list)
	images = models.JSONField(default = list)



class Event(models.Model):
	title = models.CharField(max_length = 255)
	date = models.DateTimeField(auto_now = True)
	preview = models.ImageField(upload_to = 'static/blog')
	spoiler = models.CharField(max_length = 500)
	announcement = models.BooleanField(default = False)
	image_cover = models.BooleanField(default = True)
	event = models.BooleanField(default = False)
	content = models.ForeignKey(Content, on_delete = models.CASCADE)

	def __str__(self):
		return self.title
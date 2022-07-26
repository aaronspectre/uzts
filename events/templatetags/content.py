from django import template
from events.models import ContentImage


register = template.Library()

heading = -1
image = -1
text = -1


@register.filter
def resetIndex(content):
	global heading, image, text
	heading = -1
	image = -1
	text = -1



@register.filter
def getHeading(content):
	global heading
	heading += 1
	return content.titles[heading]


@register.filter
def getText(content):
	global text
	text += 1
	return content.plains[text]


@register.filter
def getImage(content):
	global image
	image += 1
	return ContentImage.objects.get(pk = content.images[image]).image.url
import json
from django.template import Library


register = Library()


@register.filter
def read(n):
	with open('members.json', 'r') as file:
		return json.loads(file.read())
from django.shortcuts import render
from events.models import Event



def news(request):
	latest = Event.objects.all().order_by('-date')[0]
	events = Event.objects.all().order_by('-date')[1:]
	print(events)
	return render(request, 'news.html', {'events': events, 'latest': latest})


def event(request, id):
	event = Event.objects.get(pk = id)
	return render(request, 'article.html', {'event': event})
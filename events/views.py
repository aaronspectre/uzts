from django.shortcuts import render
from events.models import Event, Content, ContentImage



def news(request):
	latest = Event.objects.all().order_by('-date')[0]
	events = Event.objects.all().order_by('-date')[1:]
	print(events)
	return render(request, 'news.html', {'events': events, 'latest': latest})


def event(request, id):
	event = Event.objects.get(pk = id)
	return render(request, 'article.html', {'event': event})


def editor(request):
	return render(request, 'editor.html')


def upload(request):
	event = Event()
	event.title = request.POST['main-title']
	event.spoiler = request.POST['spoiler']
	event.preview = request.FILES['preview']

	content = Content()

	for i in range(int(request.POST['sequence'])):
		content.sequence.append(str())


	for key, value in request.POST.items():
		if 'spoiler' in key or 'main-title' in key or 'sequence' in key or 'csrfmiddlewaretoken' in key:
			continue


		ttype = key.split('-')[0]
		index = int(key.split('-')[1])
		if 'heading' in ttype:
			content.sequence[index] = ttype
			content.titles.append(value)
		elif 'text' in ttype:
			content.sequence[index] = ttype
			content.plains.append(value)


	for key, image in request.FILES.items():
		if 'preview' in key:
			continue

		ttype = key.split('-')[0]
		index = int(key.split('-')[1])
		content.sequence[index] = ttype

		content_image = ContentImage(image = image)
		content_image.save()
		content.images.append(content_image.id)


	content.save()
	event.content = content
	event.save()

	return render(request, 'editor.html')
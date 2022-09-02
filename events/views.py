from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from events.models import Event, Content, ContentImage
from main import decorators



@decorators.detector
def news(request):
	latest = Event.objects.filter(event = False).order_by('-date')[0]
	events = Event.objects.filter(event = False).order_by('-date')[1:]
	if request.session['mobile']:
		return render(request, 'mobile/news.html', {'events': events, 'latest': latest})
	return render(request, 'news.html', {'events': events, 'latest': latest})


@decorators.detector
def events(request):
	latest = Event.objects.filter(event = True).order_by('-date')[0]
	events = Event.objects.filter(event = True).order_by('-date')[1:]
	if request.session['mobile']:
		return render(request, 'mobile/news.html', {'events': events, 'latest': latest})
	return render(request, 'news.html', {'events': events, 'latest': latest})


@decorators.wrapper
def event(request, id):
	event = Event.objects.get(pk = id)
	if request.session['mobile']:
		return render(request, 'mobile/article.html', {'event': event})
	return render(request, 'article.html', {'event': event})


def editor(request):
	if request.session['mobile'] or request.user.is_anonymous:
		return HttpResponseRedirect(reverse('main:index'))
	return render(request, 'editor.html')


def upload(request):
	event = Event()
	event.title = request.POST['main-title']
	event.spoiler = request.POST['spoiler']
	event.preview = request.FILES['preview']
	event.announcement = True if 'announce' in request.POST else False
	event.event = True if 'isevent' in request.POST else False
	event.image_cover = True if 'cover' in request.POST else False

	content = Content()

	for i in range(int(request.POST['sequence'])):
		content.sequence.append(str())


	for key, value in request.POST.items():
		if key in ('spoiler', 'main-title', 'sequence', 'csrfmiddlewaretoken', 'cover', 'isevent', 'announce'):
			continue


		ttype = key.split('-')[0]
		print(key)
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
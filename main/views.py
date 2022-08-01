from django.shortcuts import render


def index(request):
	return render(request, 'index.html')


def membership(request):
	return render(request, 'membership.html')


def about(request):
	return render(request, 'about.html')


def team(request):
	return render(request, 'team.html')


def contacts(request):
	return render(request, 'contact.html')


def gallery(request):
	return render(request, 'gallery.html')


def library(request):
	return render(request, 'library.html')


def application(request):
	return render(request, 'application.html')
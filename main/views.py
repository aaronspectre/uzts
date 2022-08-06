from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from main.models import Subscriber, Member
from events.models import Event

from django.core.mail import send_mail


def index(request):
	news = Event.objects.all().order_by('-date')[:3]
	return render(request, 'index.html', {'news': news})


def membership(request):
	return render(request, 'membership.html')


def partners(request):
	return render(request, 'partners.html')


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


def instruction(request):
	return render(request, 'instruction.html')



def distribution(request):
	email = Subscriber(email = request.POST['email'])
	email.save()
	return HttpResponseRedirect(reverse('main:index'))


def mail(request):
	try:
		send_mail('Contact', request.POST['message'], 'UZTS', [request.POST['email']])
	except Exception as e:
		print(e)
	return HttpResponseRedirect(reverse('main:contacts'))



def apply(request):
	try:
		member = Member()
		member.legal_name = request.POST['legal_name']
		member.chairman = request.POST['chairman']
		member.phone = request.POST['phone']
		member.email = request.POST['email']
		member.register_date = request.POST['register_date']
		member.certificate = request.POST['certificate']
		member.tin = request.POST['tin']
		member.acsne = request.POST['acsne']
		member.activity = request.POST['activity']
		member.capital_uzs = request.POST['capital_uzs']
		member.capital_usd = request.POST['capital_usd']
		member.bank = request.POST['bank']
		member.mfo = request.POST['mfo']

		member.legal_address_city = request.POST['legal_address_city']
		member.legal_address_region = request.POST['legal_address_region']
		member.legal_address_details = request.POST['legal_address_details']
		member.legal_phone = request.POST['legal_phone']
		member.legal_fax = request.POST['legal_fax']
		member.legal_website = request.POST['legal_website']

		member.production_address_city = request.POST['production_address_city']
		member.production_address_region = request.POST['production_address_region']
		member.production_address_details = request.POST['production_address_details']

		member.production_activity = request.POST['production_activity']
		member.production_activity_details = request.POST['production_activity_details']
		member.production_activity_products = request.POST['production_activity_products']
		member.production_volume = request.POST['production_volume']
		member.production_capacity = request.POST['production_capacity']
		member.production_operating_capacity = request.POST['production_operating_capacity']
		member.production_workers_amount = request.POST['production_workers_amount']
		member.production_export = request.POST['production_export']
		member.production_products_volume_uzs = request.POST['production_products_volume_uzs']
		member.production_products_volume_usd = request.POST['production_products_volume_usd']
		member.production_markets = request.POST['production_markets']

		member.charter = request.FILES['charter']

		for key, value in request.POST.items():
			if 'founder' in key:
				member.founders.append({value: request.POST['share-'+key.split('-')[1]]})


		member.save()

	except Exception as e:
		print(e)

	return HttpResponseRedirect(reverse('main:index'))
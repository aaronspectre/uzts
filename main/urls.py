from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('distribution', views.distribution, name = 'distribution'),
	path('about-us', views.about, name = 'about'),
	path('about-us/team', views.team, name = 'team'),
	path('about-us/subsidiary', views.subsidiary, name = 'subsidiary'),
	path('contacts', views.contacts, name = 'contacts'),
	path('contacts/mail', views.mail, name = 'mail'),
	path('gallery', views.gallery, name = 'gallery'),
	path('library', views.library, name = 'library'),
	path('membership', views.membership, name = 'membership'),
	path('membership/application', views.application, name = 'application'),
	path('membership/application/save', views.apply, name = 'apply'),
	path('membership/instruction', views.instruction, name = 'instruction'),
	path('membership/partners', views.partners, name = 'partners'),
	path('membership/members', views.members, name = 'members'),
]
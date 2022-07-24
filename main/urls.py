from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('membership', views.membership, name = 'membership'),
	path('about-us', views.about, name = 'about'),
	path('team', views.team, name = 'team'),
	path('contacts', views.contacts, name = 'contacts'),
	path('gallery', views.gallery, name = 'gallery'),
	path('library', views.library, name = 'library'),
]
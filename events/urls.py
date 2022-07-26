from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
	path('', views.news, name = 'news'),
	path('view/<int:id>', views.event, name = 'view'),

	path('editor', views.editor, name = 'editor'),
	path('editor/save', views.upload, name = 'upload')
]
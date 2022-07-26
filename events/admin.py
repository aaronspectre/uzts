from django.contrib import admin
from events.models import Event, Content, ContentImage

admin.site.register(Event)
admin.site.register(Content)
admin.site.register(ContentImage)
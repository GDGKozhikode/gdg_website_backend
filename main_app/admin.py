from django.contrib import admin
from .models import Speaker, Organizer, Supporter, Event


admin.site.register(Speaker)
admin.site.register(Organizer)
admin.site.register(Supporter)
admin.site.register(Event)

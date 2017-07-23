from django.contrib import admin
from .models import Speaker, Organizer, Supporter, Event, EventImage, \
    Location, SupportFile, SocialLink


admin.site.register(Speaker)
admin.site.register(Organizer)
admin.site.register(Supporter)
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(Location)
admin.site.register(SupportFile)
admin.site.register(SocialLink)

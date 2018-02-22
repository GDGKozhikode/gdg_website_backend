from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'speaker', 'event_type', 'venue', 'date')
    fieldsets = (
        (None, {
            'fields': ('name', 'event_type', 'speaker', 'date',
                       'time', 'venue', 'description', 'photo', 'reg_link')
        }),
    )


admin.site.register(Event, EventAdmin)

from django.contrib import admin

from .models import Organizer


class OrganizerAdmin(admin.ModelAdmin):
    model = Organizer
    list_display = ('name', 'desigination', 'contact_no', 'email')
    fieldsets = (
        (None, {
            'fields': ('name', 'desigination', 'contact_no', 'email', 'photo')
        }),
        ('Social Links', {
            'fields': ('facebook', 'twitter', 'linkedin', 'google_plus', 'github', 'stackoverflow')
        }),
    )


admin.site.register(Organizer, OrganizerAdmin)

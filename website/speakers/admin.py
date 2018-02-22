from django.contrib import admin

from .models import Speaker


class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    list_display = ('name', 'designation', 'contact_no', 'email')
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'designation', 'contact_no', 'email', 'photo')
        }),
        ('Social Links', {
            'fields': ('facebook', 'twitter', 'linkedin', 'google_plus', 'github', 'stackoverflow')
        }),
    )


admin.site.register(Speaker, SpeakerAdmin)
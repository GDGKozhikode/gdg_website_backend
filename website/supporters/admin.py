from django.contrib import admin

from .models import Supporter


class SupporterAdmin(admin.ModelAdmin):
    model = Supporter
    list_display = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'photo', 'website', 'location')
        }),
    )


admin.site.register(Supporter, SupporterAdmin)

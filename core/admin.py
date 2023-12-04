from django.contrib import admin
from .models import SiteSetup


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ['header_title', 'footer_text',]
    list_display_links = ['header_title', 'footer_text',]

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()

from django.contrib import admin

from check_url.models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'status', 'update_at']

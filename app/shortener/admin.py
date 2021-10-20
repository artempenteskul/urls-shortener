from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'short_url')
    list_display_links = ('url', 'short_url')


admin.site.register(Url)

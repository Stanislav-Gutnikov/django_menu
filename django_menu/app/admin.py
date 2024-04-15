from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'named_url', 'parent_obj']
    list_filter = ['name',]
    search_fields = ['name', 'url', 'named_url']
    ordering = ['id']

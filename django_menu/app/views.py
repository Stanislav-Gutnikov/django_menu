from django.shortcuts import render
from django import template
from django.utils.safestring import mark_safe
from .models import Menu


register = template.Library()

def index(request, name):
    context = Menu.objects.filter(name=name).select_related('parent_obj')
    return render(request, 'app/index.html', {'menu_items': context})

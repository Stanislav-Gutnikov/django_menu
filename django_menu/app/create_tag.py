from django import template
from django.utils.safestring import mark_safe
from app.models import Menu


register = template.Library()

@register.simple_tag
def create_custom_tags(name):
    menu = Menu.objects.filter(name=name).select_related('parent_obj')
    return mark_safe(menu_generator(menu))


def menu_generator(menu):
    html_menu_string = '<ul>'
    for obj in menu:
        html_menu_string += '<li>'
        if obj.url:
            html_menu_string += f'<a href="{obj.url}">{obj.name}</a>'
        elif obj.named_url:
            html_menu_string += f'<a href="{obj.named_url}">{obj.name}</a>'
        else:
            html_menu_string += obj.name
        if obj.child_obj:
            html_menu_string += menu_generator(obj.child_obj.all())
        html_menu_string += '</li>'
    html_menu_string += '</ul>'
    return html_menu_string

from django import template

register = template.Library()


@register.filter(name='remove_underscore')
def remove_underscore(name):
    name=name.replace("_"," ")
    return name.capitalize()

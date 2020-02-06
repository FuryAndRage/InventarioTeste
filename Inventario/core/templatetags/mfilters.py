

from django import template
register = template.Library()


@register.filter(name='soma_valores')
def soma_valores(soma):
    pass

from urllib.parse import urlencode

from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def admin_reverse(model, action, pk=None, **kwargs):
    reverse_str = f'admin:ToDoDashboard_{model}_{action}'
    if pk:
        url = reverse(reverse_str, args=[pk])
    else:
        url = reverse(reverse_str)
    if kwargs:
        query_str = urlencode(kwargs)
        url += f'?{query_str}'
    return url

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def truncate_html_chars(value, lines):
    content_lines = value.split('\n')
    truncated_lines = content_lines[:lines]
    truncated_value = '\n'.join(truncated_lines)
    return mark_safe(truncated_value)

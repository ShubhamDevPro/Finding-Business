# Create a custom template filter
from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    # Return an empty string if the key is not found
    return dictionary.get(key, '')

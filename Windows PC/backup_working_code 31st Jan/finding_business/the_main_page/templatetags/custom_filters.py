# Create a custom template filter
from django import template
from .. import views
from django.urls import reverse
register = template.Library()

tool_dict = {
    "viewing_map": "this is the map",
    "list_of_similar_business": "here's your list",
    "suitable_location": "location is suitable",
    "analyse_transportation": "ta ta ta ta"
}
tool_dict_display = {
    "viewing_map": "View Map of the Area",
    "list_of_similar_business": "Get list of similar business in the Area",
    "suitable_location": "Find the perfect location",
    "analyse_transportation": "Analyse transportation facilities of an Area"
}
tool_list = list(tool_dict.keys())
@register.filter
def get_item(dictionary, key):
    # Return an empty string if the key is not found
    return dictionary.get(key, '')
@register.filter
def get_path(tool):
    tool_path = reverse("tools", args=[tool])
    return '//127.0.0.1:8000'+tool_path

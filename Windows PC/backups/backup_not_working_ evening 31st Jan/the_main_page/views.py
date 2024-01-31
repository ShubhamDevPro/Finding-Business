from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
tool_dict = {
    "viewing_map": "this is the map",
    "suitable_location": "location is suitable",
    "list_of_similar_business": "here's your list",
    "analyse_transportation": "ta ta ta ta"
}
tool_dict_display = {
    "viewing_map": "View Map of the Area",
    "list_of_similar_business": "Get list of similar business",
    "suitable_location": "Find the perfect location",
    "analyse_transportation": "Analyse transportation facilities"
}
tool_list = list(tool_dict.keys())


def index(request):
    try:
        return render(request, "the_main_page/main.html", {
            "tool_list": tool_list,
            "text": "The Main Page",
            "tool_dict_display": tool_dict_display,
            "tool_dict": tool_dict}
        )
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

    """
    try:
        
    except:
        return HttpResponseNotFound("This tool is unavailable yet")
"""


def tools(request, tool):
    try:
        # tool_path = reverse("tools", args=[tool])
        tool_path = reverse("tools", args=[tool])
        # tool_path = "the_main_page/tools/"+tool+".html"
        return render(request, tool_path)
        # display_text = tool_dict_display[tool]
        # return HttpResponse(display_text)
        """
        list_items = ""
        for tool1 in tool_list:
            display_text = tool_dict_display[tool1]
            tool_path = reverse("tools", args=[tool1])
            list_items += f"<li><a href =\"{tool_path}\">{display_text}</a></li><br>"
        response_data = f"<ul>{list_items}</ul>"
        return HttpResponse(response_data)
        """
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def tools_by_numbers(request, tool):
    if tool > len(tool_dict) or tool < 1:
        return HttpResponseNotFound("Tool Unavailable at the moment")
    tool_list = list(tool_dict.keys())
    redirect_tool_key = tool_list[tool-1]
    redirect_path = reverse("tools", args=[redirect_tool_key])
    return HttpResponseRedirect(redirect_path)

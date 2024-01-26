from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# HttpResponse -> Object

# Create your views here.


def main_page(request):  # a parameter "request" is passed and the function returns a response
    return HttpResponse("this is the main page")


"""
def option_1(request):
    return HttpResponse("option_1")
"""

tool_dict = {
    "viewing_map": "this is the map",
    "list_of_similar_business": "here's your list",
    "suitable_location": "location is suitable",
    "analyse_transportation": "ta ta ta ta"
}


def tools(request, tool):
    try:
        text = tool_dict[tool]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("This tool is unavailable yet")


def tools_by_numbers(request, tool):
    # .keys() returns a list of the keys of the dictionary
    if tool > len(tool_dict) or tool < 1:
        return HttpResponseNotFound("Tool Unavailable at the moment")
    tool_list = list(tool_dict.keys())
    redirect_tool_key = tool_list[tool-1]
    # will correctly build a full path to the "name"
    redirect_path = reverse("tools", args=[redirect_tool_key])

    # return HttpResponseRedirect("/team_area51_hackathon/"+redirect_tool_key)
    return HttpResponseRedirect(redirect_path)


"""
def tools(request, tool):
    if tool == "viewing_map":
        text = "here is the map"
    elif tool == "list_of_similar_business":
        text = "here's your list"
    else:
        return HttpResponseNotFound("This tool is unavailable yet")
    return HttpResponse(text)
"""

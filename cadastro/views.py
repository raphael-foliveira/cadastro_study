from http.client import HTTPResponse
from django.shortcuts import render


def home_view(request):
    response: HTTPResponse = render(
        request=request, template_name="index.html")
    return response

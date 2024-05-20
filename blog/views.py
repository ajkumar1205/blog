from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    html = """
        <title hx-swap-oob="true" hx-target="title">Blog</title>
    """
    response = HttpResponse(status=200)
    response["HX-Replace-Url"] = "/blog"
    return response
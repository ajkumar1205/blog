from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

def response(request):
    html = """
        <h1 class="text-2xl text-white">Response</h1>
    """
    return HttpResponse(html)

def blog(request):
    response = HttpResponse(render(request, "blog.html"))
    response['HX-Push-Url'] = "blog/"

    print(response)
    return response

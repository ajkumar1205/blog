from django.urls import path
from .views import Index, response, blog

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("blog/", blog, name="blog"),
    path("response/", response, name="response")
]
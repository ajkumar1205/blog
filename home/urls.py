from django.urls import path
from .views import Index, response

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("response/", response, name="response")
]
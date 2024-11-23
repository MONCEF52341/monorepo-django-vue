from django.urls import path, include
from .views import ExampleView


urlpatterns = [
    path("yes/", ExampleView.as_view())
]
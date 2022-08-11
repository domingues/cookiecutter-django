from django.urls import path

from . import views

urlpatterns = [
    path("", views.Example.as_view(), name="example"),
]

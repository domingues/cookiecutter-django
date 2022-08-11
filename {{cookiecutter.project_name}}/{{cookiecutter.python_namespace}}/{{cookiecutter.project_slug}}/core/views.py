from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class Example(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "title": "Hello world!",
        }
        return render(request, "{{cookiecutter.project_slug}}/example.html", context)

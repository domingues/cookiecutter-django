"""URL config for {{cookiecutter.project_slug}} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .storage import serve_static_files

urlpatterns = i18n_patterns(
    path("", include("{{cookiecutter.python_namespace}}.{{cookiecutter.project_slug}}.core.urls")),
    path("admin/", admin.site.urls),
)
urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += serve_static_files()
urlpatterns += debug_toolbar_urls()

from django.conf import settings
from django.urls import get_script_prefix, path
from django.views.static import serve


def serve_static_files():
    if settings.SERVE_STATIC_FILES and not settings.DEBUG:
        route = (
            f'{settings.STATIC_URL.removeprefix(get_script_prefix()).lstrip("/")}'
            f"<path:path>"
        )
        return [path(route, serve, kwargs={"document_root": settings.STATIC_ROOT})]
    return []

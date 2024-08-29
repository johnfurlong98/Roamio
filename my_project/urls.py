"""
URL configuration for the my_project project.

This module defines the URL patterns for the entire project, mapping URLs
to their corresponding views. It includes the URL patterns for the admin
interface, authentication, and app-specific URLs.

For more information, see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

URL Patterns:
    - "admin/": Routes to the Django admin interface.
    - "accounts/": Routes to the authentication URLs provided by `allauth`.
    - "": Includes URLs from the `destinations` app.
    - "": Includes URLs from the `home` app.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from destinations import views as destinations_views  # Ensure correct import here
from users import views as users_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("destinations.urls")),  # Include the destinations app URLs
    path("", include("home.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

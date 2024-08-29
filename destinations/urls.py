from django.urls import path
from destinations import views

"""
URL configuration for the Destinations app.

This module defines the URL patterns for accessing various views related
to destinations and comments. It maps URLs to their corresponding view methods.

URL Patterns:
    - "destinations/": List all destinations or create a new destination.
    - "destinations/<id>": Retrieve, update, or delete a specific destination.
    - "destinations-list/": Render a template to list all destinations.
    - "destination-details/<id>": Render a template for detailed view of a destination.
    - "destinations-form/": Render a template for creating or updating a destination.
    - "comments/": List all comments or create a new comment.
    - "comments/<id>": Retrieve, update, or delete a specific comment.
"""

urlpatterns = [
    path(
        "destinations/",
        views.DestinationViewset.as_view({"get": "get_queryset", "post": "create"}),
        name="destination-list-create",
    ),
    path(
        "destinations/<id>",
        views.DestinationViewset.as_view(
            {"patch": "partial_update", "delete": "delete"}
        ),
        name="destination-detail",
    ),
    path(
        "destinations-list/",
        views.DestinationTemplates.as_view({"get": "get_destination_list"}),
        name="destinations-list",
    ),
    path(
        "destination-details/<id>",
        views.DestinationTemplates.as_view(
            {"get": "get_destination_detail", "post": "get_destination_detail"}
        ),
        name="destination-detail",
    ),
    path(
        "destinations-form/",
        views.DestinationTemplates.as_view(
            {"get": "get_destination_form", "post": "get_destination_form"}
        ),
        name="destination-form",
    ),
    path(
        "comments/",
        views.CommentViewSet.as_view({"get": "get_queryset", "post": "create"}),
        name="comment-list-create",
    ),
    path(
        "comments/<id>",
        views.CommentViewSet.as_view({"patch": "partial_update", "delete": "delete"}),
        name="comment-detail",
    ),
]

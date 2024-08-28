from django.urls import path
from destinations import views


from .views import (
    Destination,
)


urlpatterns = [
    # path('', views.destination_list, name='destination_list'),
    # path('<int:pk>/', views.destination_detail, name='destination_detail'),
    # path('new/', views.destination_create, name='destination_create'),
    path(
        "destinations/",
        views.DestinationViewset.as_view({"get": "get_queryset", "post": "create"}),
    ),
    path(
        "destinations/<id>",
        views.DestinationViewset.as_view(
            {"patch": "partial_update", "delete": "delete"}
        ),
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
    ),
    path(
        "comments/",
        views.CommentViewSet.as_view({"get": "get_queryset", "post": "create"}),
    ),
    path(
        "comments/<id>",
        views.CommentViewSet.as_view({"patch": "partial_update", "delete": "delete"}),
    ),
]

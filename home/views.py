from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action

from destinations.models import Destination
from destinations.serializers import DestinationSerializer


class HomeViewSet(viewsets.ViewSet):
    """
    ViewSet for handling home-related views and actions.

    This ViewSet provides actions for retrieving a list of destinations. It is
    used to handle requests related to displaying destinations in the home view.

    Actions:
        - `destination_list`: Retrieve and return a list of all destinations
          serialized in JSON format, rendered in the home page.
    """

    @action(detail=False, methods=["get"])
    def destination_list(self, request):
        """
        Retrieve and return a list of all destinations.

        This action retrieves all destination objects, serializes them using
        `DestinationSerializer`, and renders them in the "home/index.html" template.

        Args:
            request: The HTTP request object.

        Returns:
            A rendered HTML response containing the list of destinations.
        """
        destinations = Destination.objects.all()
        serialized_data = DestinationSerializer(destinations, many=True).data
        return render(request, "home/index.html", {"destinations": serialized_data})


def index(request):
    """
    Display the home page with the top liked destinations.

    This function retrieves the top 3 destinations ordered by the number of likes,
    serializes them using `DestinationSerializer`, and renders them in the
    "home/index.html" template.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response containing the top liked destinations and Cloudinary
        cloud name for image rendering.
    """
    top_liked_destinations = Destination.objects.order_by("-likes")[:3]
    serialized_data = DestinationSerializer(top_liked_destinations, many=True).data
    print(serialized_data)
    return render(
        request,
        "home/index.html",
        {
            "destination_list": serialized_data,
            "cloud_name": settings.CLOUDINARY_CLOUD_NAME,
        },
    )

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from destinations.models import Destination
from destinations.serializers import DestinationSerializer


class HomeViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def destination_list(self, request): 
        destinations = Destination.objects.all()
        serialized_data = DestinationSerializer(destinations, many=True).data
        return render(request, 'home/index.html', {"destinations": serialized_data})

def index(request):
    return render(request, 'home/index.html')
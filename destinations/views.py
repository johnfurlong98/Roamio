from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.decorators import login_required
from .forms import DestinationForm
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DestinationSerializer

class DestinationViewset(viewsets.ModelViewSet):

    serializer_class = DestinationSerializer
    queryset = Destination.objects.none()

    def get_queryset(self, request):
        id = request.query_params.get('id', None)
        queryset = Destination.objects.all()
        if id: 
            queryset = queryset.filter(id=id)
        
        data = DestinationSerializer(queryset, many=True).data
        
        return Response(data)
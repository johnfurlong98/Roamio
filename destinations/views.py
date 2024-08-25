from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.decorators import login_required
from .forms import DestinationForm
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DestinationSerializer
from django.contrib.auth.models import User
from django.utils import timezone 

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

    def create(self, request):
        try:
            name = request.data['name']
            location = request.data['location']
            email = request.data['email']
            description = request.data['description']

        except Exception as e: 
            print(e)
            return HttpResponse('Missing Data')

        created_on = request.data.get('created_on', timezone.now())
        status = request.data.get('status', 1)

        try: 
            user = User.objects.get(email=email)
        except:
            return HttpResponse('Missing User')
        try:
            new_destination = Destination.objects.get(name=name)
            return HttpResponse('Destination already exists')
        except:
            new_destination = Destination.objects.create(
                name=name,
                location=location,
                author=user,
                created_on=created_on,
                description=description,
                status=status
            )
        data = DestinationSerializer(new_destination).data

        return Response(data)


    def partial_update(self, request, id):
        status = request.data.get('status', 1)

        if not id:
            return HttpResponse('No id provided')

        try:
            destination = Destination.objects.get(id=id)
        except:
            return HttpResponse('Destination does not exist')

        destination.status = status 
        destination.save()

        return HttpResponse('Destination Updated!')


    def delete(self, request, id):
        if not id:
            return HttpResponse('No id provided')

        try:
            destination = Destination.objects.get(id=id)
        except:
            return HttpResponse('Destination does not exist')

        destination.delete()
        return HttpResponse('Destination Deleted')
        


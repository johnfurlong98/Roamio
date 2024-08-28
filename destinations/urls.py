from django.urls import path
from destinations import views


from.views import (
    Destination,
)


urlpatterns = [
    # path('', views.destination_list, name='destination_list'),
    # path('<int:pk>/', views.destination_detail, name='destination_detail'),
    # path('new/', views.destination_create, name='destination_create'),
    path('destinations/', views.DestinationViewset.as_view({'get': 'get_queryset', 'post': 'create'})),
    path('destinations/<id>', views.DestinationViewset.as_view({'patch': 'partial_update', 'delete': 'delete'})),
    
    path('destinations-list/', views.DestinationTemplates.as_view({'get': 'get_destination_list'})),
    path('destination-details/<id>', views.DestinationTemplates.as_view({'get': 'get_destination_detail'})),
    
    path('destinations-form/', views.DestinationTemplates.as_view({'get': 'get_destination_form', 'post': 'get_destination_form'})),


]
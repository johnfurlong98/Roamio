from django.urls import path
from destinations import views


from.views import (
    Destination,
)


urlpatterns = [
    # path('', views.destination_list, name='destination_list'),
    # path('<int:pk>/', views.destination_detail, name='destination_detail'),
    # path('new/', views.destination_create, name='destination_create'),
    path('destinations/', views.DestinationViewset.as_view({'get': 'get_queryset'}))
]

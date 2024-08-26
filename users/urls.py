from django.urls import path
from .views import login_view  # Import your login view function or class

urlpatterns = [
    # Other URL patterns
    path('login/', login_view, name='account_login'),
]
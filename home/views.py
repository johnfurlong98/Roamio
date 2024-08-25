from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from destinations.models import Destination

class IndexView(TemplateView):
    template_name = "home/index.html"

class DestinationsListView(TemplateView):
    template_name = "home/destinations_list.html"

class RegisterView(TemplateView):
    template_name = "home/register.html"

class LoginView(TemplateView):
    template_name = "home/login.html"

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.shortcuts import render


# Create your views here.
#def profile(request):
 #   return HttpResponse("This would be the user profile page")

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

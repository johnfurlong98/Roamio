from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.shortcuts import render


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

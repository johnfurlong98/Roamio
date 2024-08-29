from django.contrib import admin
from django.urls import path
from home import views

"""
    URL configuration for the Home app.

    This module defines the URL patterns for the 'home' application. It maps
    URLs to their corresponding view functions.

    URL Patterns:
        - "": Maps to the index view of the Home app.
"""
urlpatterns = [
    path("", views.index, name="index"),
]

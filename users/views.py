"""
ViewSets for managing `User` instances.

This module defines the viewsets for handling `User` model instances
using Django REST framework. It includes methods for listing, creating,
retrieving, updating, and deleting users.
"""

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling `User` instances.

    This viewset provides CRUD operations for the `User` model, including
    listing all users, retrieving a specific user, creating new users,
    updating existing users, and deleting users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

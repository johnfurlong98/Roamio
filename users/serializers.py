"""
Serializers for the `User` model.

This module contains serializers for the `User` model provided by Django's
auth module. Serializers are used to convert model instances to and from
JSON format.
"""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the `User` model.

    This serializer is used to convert `User` model instances to JSON format
    and validate input data for creating or updating `User` instances.
    """

    class Meta:
        model = User
        fields = [
            "username",
        ]

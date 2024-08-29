from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Destination, Comment
from users.serializers import UserSerializer


class DestinationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Destination model.

    This serializer converts the Destination model instances to JSON and vice versa.
    It includes all fields of the Destination model and nests the UserSerializer
    for the 'author' field.

    Attributes:
        author (UserSerializer): A nested serializer for the author of the destination.
    """

    author = UserSerializer(read_only=True)

    class Meta:
        model = Destination
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    This serializer converts the Comment model instances to JSON and vice versa.
    It includes all fields of the Comment model.

    Attributes:
        None
    """

    class Meta:
        model = Comment
        fields = "__all__"

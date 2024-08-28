from rest_framework import serializers
from .models import Destination, Comment
from users.serializers import UserSerializer
from django.contrib.auth.models import User


class DestinationSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Destination
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from .models import Destination, Comment, UserDestinationLikes, UserCommentLikes
from .forms import DestinationForm, CommentForm


# Create your tests here.
class DestinationViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        self.destination_data = {
            "name": "Test Destination",
            "location": "Test Location",
            "description": "Test Description",
            "email": self.user.email,
        }
        self.client.login(username="testuser", password="testpass")

    def test_create_destination(self):
        response = self.client.post(
            reverse("destination-list"), data=self.destination_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.count(), 1)
        self.assertEqual(Destination.objects.first().name, "Test Destination")

    def test_get_destination_list(self):
        Destination.objects.create(
            name="Test Destination",
            location="Test Location",
            author=self.user,
            description="Test Description",
        )
        response = self.client.get(reverse("destination-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Destination")


def test_like_destination(self):
    destination = Destination.objects.create(
        name="Test Destination",
        location="Test Location",
        author=self.user,
        description="Test Description",
    )
    response = self.client.patch(reverse("destination-detail", args=[destination.id]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(Destination.objects.first().likes, 1)

    def test_delete_destination(self):
        destination = Destination.objects.create(
            name="Test Destination",
            location="Test Location",
            author=self.user,
            description="Test Description",
        )
        response = self.client.delete(
            reverse("destination-detail", args=[destination.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.count(), 0)


class CommentViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        self.destination = Destination.objects.create(
            name="Test Destination",
            location="Test Location",
            author=self.user,
            description="Test Description",
        )
        self.comment_data = {
            "destination": self.destination.id,
            "user": self.user.id,
            "text": "Test Comment",
        }
        self.client.login(username="testuser", password="testpass")

    def test_create_comment(self):
        response = self.client.post(reverse("comment-list"), data=self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().text, "Test Comment")

    def test_get_comment_list(self):
        Comment.objects.create(
            destination=self.destination, user=self.user, text="Test Comment"
        )
        response = self.client.get(reverse("comment-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["text"], "Test Comment")

    def test_like_comment(self):
        comment = Comment.objects.create(
            destination=self.destination, user=self.user, text="Test Comment"
        )
        response = self.client.patch(reverse("comment-detail", args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.first().likes, 1)

    def test_delete_comment(self):
        comment = Comment.objects.create(
            destination=self.destination, user=self.user, text="Test Comment"
        )
        response = self.client.delete(reverse("comment-detail", args=[comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 0)

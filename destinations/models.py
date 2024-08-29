from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Destination(models.Model):
    """
    Model representing a travel destination.

    Attributes:
        name (str): The name of the destination (unique).
        description (str): A detailed description of the destination.
        location (str): The location of the destination.
        featured_image (CloudinaryField): An optional image for the destination, stored in Cloudinary.
        author (User): The user who created the destination.
        created_on (DateTimeField): Timestamp when the destination was created.
        status (int): Status of the destination, where 0 is inactive and 1 is active.
        likes (int): Number of likes the destination has received.
    """

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    featured_image = CloudinaryField("image", default="placeholder")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_destinations"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=[(0, "Inactive"), (1, "Active")], default=1)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Model representing a comment on a destination.

    Attributes:
        destination (Destination): The destination that the comment is associated with.
        user (User): The user who made the comment.
        created_on (DateTimeField): Timestamp when the comment was created.
        text (str): The content of the comment.
        likes (int): Number of likes the comment has received.
    """

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)


class UserCommentLikes(models.Model):
    """
    Model representing a like on a comment by a user.

    Attributes:
        user (User): The user who liked the comment.
        comment (Comment): The comment that was liked.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class UserDestinationLikes(models.Model):
    """
    Model representing a like on a destination by a user.

    Attributes:
        user (User): The user who liked the destination.
        destination (Destination): The destination that was liked.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

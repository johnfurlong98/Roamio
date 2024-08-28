from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)  # The name of the destination
    description = models.TextField()  # A detailed description of the destination
    location = models.CharField(max_length=200)  # The location of the destination
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_destinations"
    )  # The user who created the destination
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp when the destination was created
    status = models.IntegerField(choices=[(0, "Inactive"), (1, "Active")], default=1)  # Status of the destination
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)


class UserCommentLikes(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class UserDestinationLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE) 


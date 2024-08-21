from django.db import models
from django.contrib.auth.models import User

class destination(models.Model):
    name = models.CharField(max_length=200, unique=True)  # The name of the destination
    description = models.TextField()  # A detailed description of the destination
    location = models.CharField(max_length=200)  # The location of the destination
    image = models.ImageField(upload_to='destination_images/', null=True, blank=True)  # Image for the destination
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_destinations"
    )  # The user who created the destination
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp when the destination was created
    status = models.IntegerField(choices=[(0, "Inactive"), (1, "Active")], default=1)  # Status of the destination

    def __str__(self):
        return self.name

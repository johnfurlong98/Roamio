from django import forms
from .models import Destination


class DestinationForm(forms.Form):
    """
    Form for creating or updating a Destination.

    This form is used to collect and validate data for the Destination model,
    including fields for the destination's name, location, description, and an
    optional image.
    """

    name = forms.CharField()
    location = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField(required=False)


class CommentForm(forms.Form):
    """
    Form for submitting a comment.

    This form is used to collect and validate the text of a comment, with a
    maximum length of 200 characters.
    """

    text = forms.CharField(max_length=200)

"""
Django application configuration for the Destinations app.

This module contains the configuration settings for the Destinations
application within the Django project. It defines the app's name and
the default field type for auto-generated primary keys.
"""

from django.apps import AppConfig


class DestinationsConfig(AppConfig):
    """
    Configuration for the Destinations application.

    This class sets up the configuration for the Destinations app,
    specifying the app's name and default settings for primary key fields.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "destinations"

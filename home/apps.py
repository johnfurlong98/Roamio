from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' Django application.

    This class is used to configure settings for the 'home' app, including
    the default auto field type and the app name. The default auto field
    type is set to 'BigAutoField' to ensure that primary keys are automatically
    generated as big integers.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary
            key fields for models in this app.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

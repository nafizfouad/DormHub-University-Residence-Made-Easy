from django.apps import AppConfig

class ProvostConfig(AppConfig):
    """
    AppConfig class for configuring the Provost app.

    Attributes:
        default_auto_field (str): The name of the field to use for automatic primary key incrementation.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Default primary key field type
    name = 'Provost'  # Name of the application

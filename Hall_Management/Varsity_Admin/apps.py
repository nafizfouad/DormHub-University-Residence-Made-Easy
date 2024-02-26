from django.apps import AppConfig


class VarsityAdminConfig(AppConfig):
    """
    AppConfig class for configuring the Varsity_Admin app.

    Attributes:
        default_auto_field (str): Specifies the default auto field to use for models in the app.
        name (str): Specifies the name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Varsity_Admin'

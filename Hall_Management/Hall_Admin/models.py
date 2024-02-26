from django.db import models


class HallAdmin(models.Model):
    """
    Model representing a Hall Admin.

    Attributes:
        adminId (int): The unique identifier for the hall admin.
        name (str): The name of the hall admin.
        email (str): The email address of the hall admin.
        username (str): The username of the hall admin.
        password (str): The password of the hall admin.
    """
    adminId = models.IntegerField(default=1, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        """
        String representation of the HallAdmin object.
        """
        return str(self.email)

from django.contrib import admin
from .models import Hall, VarsityAdmin, Room

# Register the models in the Django admin site
admin.site.register(Hall)         # Register the Hall model
admin.site.register(VarsityAdmin) # Register the VarsityAdmin model
admin.site.register(Room)         # Register the Room model

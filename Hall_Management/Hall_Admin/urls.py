"""
Django URL Configuration Documentation

This module defines URL patterns for various views and static/media file serving during development.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# Define URL patterns
urlpatterns = [
    path('', views.hallAdmin, name='hallAdmin'),  # URL pattern for the hall admin view
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

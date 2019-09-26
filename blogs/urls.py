"""URLs for the blog application."""
from django.urls import path
from . import views

urlpatterns = [  # pylint: disable=invalid-name
    path('', views.index, name='index')
]

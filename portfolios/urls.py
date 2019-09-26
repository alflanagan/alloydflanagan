"""URLs for the portfolio app."""
from django.urls import path
from . import views

urlpatterns = [  # pylint: disable=invalid-name
    path('', views.index, name='index')
]

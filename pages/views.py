"""Views which display (relatively) static pages"""
from django.shortcuts import render
from django import get_version

def about_me(request):
    """Simple About Me page"""
    return render(request, "pages/about_me.html", context={"django_version": get_version()})

def home(request):
    """Initial view for users"""
    return render(request, "pages/home.html", context={"django_version": get_version()})

def contact(request):
    """My contact information page"""
    return render(request, "pages/contact.html", context={"django_version": get_version()})

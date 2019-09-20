"""Views which display (relatively) static pages"""
from django.shortcuts import render

def about_me(request):
    """Simple About Me page"""
    return render(request, "pages/about_me.html")

def home(request):
    """Initial view for users"""
    return render(request, "pages/home.html")

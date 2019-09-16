"""Views of the blog app"""

from django.shortcuts import render

# Create your views here.
def index(request):
    """Simple view of blog titles, etc."""
    return render(request, 'blogs/index.html')

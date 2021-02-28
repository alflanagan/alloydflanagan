"""Views of the blog app"""
from rest_framework import viewsets
from rest_framework import permissions

from .models import BlogEntry, Category
from .serializers import CategorySerializer, BlogEntrySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog entries to be viewed or edited.
    """
    queryset = BlogEntry.objects.all().order_by('updated')
    serializer_class = BlogEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

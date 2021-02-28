"""Serializers for REST APIs"""

from rest_framework import serializers

from .models import BlogEntry, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class BlogEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ['title', 'content', 'created', 'updated', 'categories']

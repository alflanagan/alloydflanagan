from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=60, primary_key=True)

class BlogEntry(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category")

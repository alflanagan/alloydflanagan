from django.db import models
# pylint: disable no-member

# Create your models here.
class Category(models.Model):
    """Organize blog entries by topic"""
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
    title = models.CharField(max_length=60, primary_key=True)
    def __str__(self) -> str:
        return self.title

class BlogEntry(models.Model):
    """A blog entry, with markdown support, etc."""
    class Meta:
        ordering = ['created']
        verbose_name_plural = "Blog Entries"
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category")
    def __str__(self) -> str:
        return f"{self.title} ({self.created.date()})"

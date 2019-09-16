from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=60, primary_key=True)
    sub_title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    main_image = models.ImageField()
    thumb_image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    position = models.IntegerField(default=-1)

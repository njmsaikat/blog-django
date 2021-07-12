from django.db import models
from django.db.models.fields import SlugField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumb
    # author

    def __str__(self):
        return self.title

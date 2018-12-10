from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def preview(self):
        return self.body[0:25]+"..."

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering =['-release_date']

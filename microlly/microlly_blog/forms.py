from django import forms
from microlly_blog import models

class PostCreate(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug']

class PostEdit(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']
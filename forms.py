from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('topic',)

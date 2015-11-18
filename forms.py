from django import forms

class PostForm(forms.Form):
    content = forms.CharField(label='Message \n', max_length=10000, widget=forms.Textarea)

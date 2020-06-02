from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # ModelForm allows creating fields for the form
    class Meta:
        model = Post
        # Fields:
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # form-control is a class from bootstrap
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your text here'}),
        }






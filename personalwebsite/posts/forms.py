from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here',
                'rows': 8
            })
        }

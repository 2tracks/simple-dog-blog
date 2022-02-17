from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='Comment')
    class Meta:
        model = Comment
        
        fields = (
            'name',
            'body'
            )
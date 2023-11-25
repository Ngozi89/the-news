from .models import Comment
from django import forms


# create form class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

from .models import Comment
from django import forms                     
from cloudinary.forms import CloudinaryFileField


# create form class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

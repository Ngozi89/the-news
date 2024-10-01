from .models import Comment, Profile, Post
from django import forms                     
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):
    """
    Create Article Form
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle', 
            'details',
            'pub_time',
            'featured_image',
        ]


class ProfileForm(forms.ModelForm):
    
    class Meta:
            model = Profile
            fields = [ 'user', 'bio',]


# create form class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)      

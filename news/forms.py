from .models import Comment, Profile, Post
from django import forms                     
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):
    """
    Create Post/Article Form
    """ 
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle', 
            'details',
            'pub_time',
            'status',
            'featured_image',
        ]
        widgets = {
            'subtile': SummernoteWidget(),
            'details': SummernoteWidget(),
        }


class ProfileForm(forms.ModelForm):
    """
    Create Profile Form
    """
    class Meta:
            model = Profile
            fields = [ 'user', 'bio',]


class CommentForm(forms.ModelForm):
    """
    Comment create form class
    """
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})
    
    class Meta:
        model = Comment
        fields = ('name', 'body',)      

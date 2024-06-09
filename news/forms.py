from .models import Comment, Reply, Profile
from django import forms                     
from cloudinary.forms import CloudinaryFileField


class ProfileForm(forms.ModelForm):
    
    class Meta:
            model = Profile
            fields = [ 'user', 'bio',]


# create form class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)        

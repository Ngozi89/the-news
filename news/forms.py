from .models import Comment, Ads
from django import forms


# create form class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = ('name', 'email_address', 'phone', 'image', 'discription')
        labels = {
            'name': '',
            'email_address': '',
            'phone': '',
            'image': '',
            'description': '',
        }
widgets = {
    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'})
    'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
    'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'})
    'image': forms.MediaInput(attrs={'class':'form-control', 'placeholder':'Image'})
    'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'})
}        
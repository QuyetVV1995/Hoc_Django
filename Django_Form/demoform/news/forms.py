from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content','time_create',}          # Them cac thuoc tinh cua Post de hien thi

class sendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)


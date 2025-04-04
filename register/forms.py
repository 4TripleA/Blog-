from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from register.models import blogpost, profilepage

class adduserform(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class Loginform(forms.Form):   
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Input your password"})) 

class newblogform(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Input your News Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'content', 'placeholder': 'Enter news'}))

    class Meta:
        model = blogpost
        fields = "__all__"

class editprofileform(forms.Form):
    bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a Bio'}), required=False)
    location = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Add your Location'}), required=False)

    class Meta:
        model = profilepage
        fields = "__all__"





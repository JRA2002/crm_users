from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Client
from django import forms

class LoginForm(AuthenticationForm):
    pass
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["user","motive", "title","description"]

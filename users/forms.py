from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Client,Claim
from django import forms


class LoginForm(AuthenticationForm):
    pass
class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['product','title', 'description']
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='first_name')
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def clean_email(self):
            email_field = self.cleaned_data['email']

            if User.objects.filter(email=email_field).exists():
                raise forms.ValidationError('this email already exist')
            return email_field
    def clean_username(self):
         username_field = self.cleaned_data['username']

         if User.objects.filter(username=username_field).exists():
              raise forms.ValidationError('This username already exist')
         return username_field
         
    

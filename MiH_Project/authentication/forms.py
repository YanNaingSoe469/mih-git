from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=100, label="Email", required=True)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','name', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ChangePasswordForm(forms.Form):
    old_password = forms.EmailField(label='New Password', max_length=100, required=True)
    new_password = forms.CharField(label='Old Password', max_length=100, required=True)
    confirm_password = forms.CharField(label='Confirm New Password', max_length=100, required=True)
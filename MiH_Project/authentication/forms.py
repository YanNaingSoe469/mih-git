from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=100, label="Email", required=True)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["id", "name", "phone", "address", "profile_pic"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")

        if not phone:
            return ""

        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")

        if len(phone) < 7 or len(phone) > 15:
            raise forms.ValidationError("Phone number length is invalid.")

        return phone


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
        min_length=8,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )

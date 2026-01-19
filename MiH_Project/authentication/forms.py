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
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("Name cannot be empty.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if not phone:
            return phone

        phone = phone.replace(" ", "")

        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")

        if len(phone) < 7 or len(phone) > 20:
            raise forms.ValidationError(
                "Phone number length must be between 7 and 20 digits."
            )

        return phone


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Old password is incorrect")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        old = cleaned_data.get("old_password")
        new = cleaned_data.get("new_password")
        confirm = cleaned_data.get("confirm_password")

        if old and new and old == new:
            self.add_error("new_password", "Old password and New password are the same")

        if new and confirm and new != confirm:
            self.add_error(
                "confirm_password", "New password and Confirm password do not match"
            )

        return cleaned_data

    def save(self):
        self.user.set_password(self.cleaned_data["new_password"])
        self.user.save()

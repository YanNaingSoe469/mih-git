from django import forms
from projects_app.models import Language, Framework, Component, Focus, Algorithm
from admin_app.models import Announcement, Contact


class CreateLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"

class CreateFrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = "__all__"

class CreateComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = "__all__"

class CreateFocusForm(forms.ModelForm):
    class Meta:
        model = Focus
        fields = "__all__"

class CreateAlgorithmForm(forms.ModelForm):
    class Meta:
        model = Algorithm
        fields = "__all__"

class CreateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
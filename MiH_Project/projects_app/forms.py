import django.forms as forms
from projects_app.models import Project, Software, Hardware, Ai


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'

class SoftwareCreateForm(forms.ModelForm):
    class Meta:
        model = Software
        fields ='__all__'

class HardwareCreateForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields ='__all__'

class AiCreateForm(forms.ModelForm):
    class Meta:
        model = Ai
        fields ='__all__'
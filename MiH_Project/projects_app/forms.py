import django.forms as forms
from django.core.exceptions import ValidationError
from projects_app.models import Project, Software, Hardware, Ai


class ProjectValidationMixin:
    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()

        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")

        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()

        if len(description) < 30:
            raise ValidationError("Description must be at least 30 characters long.")

        return description

    def clean_duration(self):
        duration = self.cleaned_data.get("duration")

        if duration is None or duration <= 0:
            raise ValidationError("Duration must be a positive number.")

        # max 5 years (weeks)
        if duration > 260:
            raise ValidationError("Duration is unrealistically high.")

        return duration

    def clean_cover_photo(self):
        photo = self.cleaned_data.get("cover_photo")

        if not photo:
            raise ValidationError("Cover photo is required.")

        return photo


class ProjectCreateForm(ProjectValidationMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class SoftwareCreateForm(ProjectValidationMixin, forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        exclude = ['innovator']

    def clean_source_link(self):
        source_link = self.cleaned_data.get("source_link")

        if source_link and not source_link.startswith("https://"):
            raise ValidationError("Source link must start with https://")

        return source_link

    def clean(self):
        cleaned_data = super().clean()
        project_type = cleaned_data.get("type")

        if project_type != "SW":
            raise ValidationError("Invalid project type for Software project.")

        return cleaned_data


class HardwareCreateForm(ProjectValidationMixin, forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'
        exclude = ['innovator']

    def clean_code(self):
        code = self.cleaned_data.get("code")

        if code and not code.startswith("https://"):
            raise ValidationError("Code must start with https://")

        return code

    def clean_components(self):
        components = self.cleaned_data.get("components")

        if not components or components.count() < 1:
            raise ValidationError("Select at least one component.")

        return components

    def clean(self):
        cleaned_data = super().clean()
        project_type = cleaned_data.get("type")

        if project_type != "HW":
            raise ValidationError("Invalid project type for Hardware project.")

        return cleaned_data


class AiCreateForm(ProjectValidationMixin, forms.ModelForm):
    class Meta:
        model = Ai
        fields = '__all__'
        exclude = ['innovator']

    def clean_algorithms(self):
        algorithms = self.cleaned_data.get("algorithms")

        if not algorithms or algorithms.count() < 1:
            raise ValidationError("Select at least one algorithm.")

        return algorithms

    def clean(self):
        cleaned_data = super().clean()

        project_type = cleaned_data.get("type")
        dataset_link = cleaned_data.get("dataset_link")
        notebook_link = cleaned_data.get("notebook_source_link")

        if project_type != "AI":
            raise ValidationError("Invalid project type for AI project.")

        if dataset_link and notebook_link and dataset_link == notebook_link:
            raise ValidationError("Dataset link and notebook link must be different.")

        return cleaned_data

from django.conf import settings
from django.db import models

# Create your models here.

class Project(models.Model):
    project_types = [
        ('SW', 'Software'),
        ('HW', 'Hardware'),
        ('AI', 'AI'),
    ]

    title = models.CharField(max_length=100)
    innovator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_innovator",
    )
    cover_photo = models.ImageField(upload_to="project_covers/")
    description = models.TextField()
    duration = models.FloatField()
    type = models.CharField(max_length=10, choices=project_types)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Languages"

class Framework(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Frameworks"

class Software(Project):
    platform_types = [
        ('WEB', 'Web'),
        ('MOB', 'Mobile'),
        ('DES', 'Desktop'),
        ('CRS', 'Cross Platform'),
    ]
    source_link = models.URLField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="built_with")
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name="written_with")
    platform = models.CharField(max_length=10, choices=platform_types)

    class Meta:
        verbose_name_plural = "Software"

    def __str__(self):
        return self.title


class Component(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Components"

class Hardware(Project):
    levels = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    ]
    code = models.URLField()
    components = models.ManyToManyField(Component, related_name="consists_of")
    skill_level = models.CharField(max_length=20, choices=levels)

    class Meta:
        verbose_name_plural = "Hardware"

    def __str__(self):
        return self.title

class Focus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Focuses"

class Algorithm(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Algorithms"

class Ai(Project):
    dataset_link = models.URLField()
    notebook_source_link = models.URLField()
    algorithms = models.ManyToManyField(Algorithm, related_name="applies")
    focus = models.ForeignKey(Focus, on_delete=models.CASCADE, related_name="has")
    class Meta:
        verbose_name_plural = "Ai"

    def __str__(self):
        return self.title
from django.contrib import admin

from projects_app.models import (Project, Language, Framework, Software, Component, Hardware, Focus, Algorithm, Ai)


# Register your models here.
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Software)
admin.site.register(Component)
admin.site.register(Hardware)
admin.site.register(Focus)
admin.site.register(Algorithm)
admin.site.register(Ai)

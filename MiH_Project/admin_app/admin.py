from django.contrib import admin

from admin_app.models import Contact, Announcement

# Register your models here.
admin.site.register(Contact)
admin.site.register(Announcement)
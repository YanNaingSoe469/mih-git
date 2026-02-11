from django.contrib import admin

from feedback_app.models import Comment, Rating

admin.site.register(Comment)
admin.site.register(Rating)

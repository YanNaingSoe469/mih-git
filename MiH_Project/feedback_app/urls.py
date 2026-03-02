from authentication import views as authentication_views
from projects_app import views as project_views
from admin_app import views as admin_views
from feedback_app import views as feedback_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('add-comment/<int:project_id>/', feedback_views.add_comment, name="add_comment"),
    path('comment/delete/<int:comment_id>/', feedback_views.delete_comment, name='delete_comment'),
    path('add-rating/<int:project_id>/', feedback_views.add_rating, name="add_rating"),
]
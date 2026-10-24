from authentication import views as authentication_views
from projects_app import views as project_views
from admin_app import views as admin_views
from feedback_app import views as feedback_views

from django.urls import path


urlpatterns = [
path("sw-create/", project_views.create_software, name="sw_create"),
    path("hw-create/", project_views.create_hardware, name="hw_create"),
    path("ai-create/", project_views.create_ai, name="ai_create"),

    path('project-detail/<int:id>/', project_views.project_detail, name="project_detail"),
    path('project-search/', authentication_views.user_homepage, name="search_project"),

    path('sw-update/<int:id>', project_views.update_software, name="sw_update"),
    path('hw-update/<int:id>', project_views.update_hardware, name="hw_update"),
    path('ai-update/<int:id>', project_views.update_ai, name="ai_update"),

    path('project-delete/<int:id>/', project_views.project_delete, name="project_delete"),
]
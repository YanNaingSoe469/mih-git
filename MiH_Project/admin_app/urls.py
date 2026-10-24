from authentication import views as authentication_views
from projects_app import views as project_views
from admin_app import views as admin_views
from feedback_app import views as feedback_views

from django.urls import path

urlpatterns = [
    path("user-list/", authentication_views.user_list, name="user_list"),
    path("project-list/", admin_views.project_list, name="project_list"),
    path("project-stats/", admin_views.project_stats, name="project_stats"),
    path('grant-admin/<int:id>/', admin_views.grant_admin, name="grant_admin"),
    path('revoke-admin/<int:id>/', admin_views.revoke_admin, name="revoke_admin"),
    path('create-announcement/', admin_views.create_announcement, name="create_announcement"),
    path('delete-announcement/<int:id>/', admin_views.delete_announcement, name="delete_announcement"),
    path('update-announcement/<int:id>/', admin_views.update_announcement, name="update_announcement"),
    path('create-contact/', admin_views.create_contact, name="create_contact"),
    path('contact-list/', admin_views.contact_list, name="contact_list"),

    # language operations
    path('language-create/', admin_views.create_language, name="create_language"),
    path('language-update/<int:id>/', admin_views.update_language, name="update_language"),
    path('language-delete/<int:id>/', admin_views.delete_language, name="delete_language"),

    # framework operations
    path('framework-create/', admin_views.create_framework, name="create_framework"),
    path('framework-update/<int:id>/', admin_views.update_framework, name="update_framework"),
    path('framework-delete/<int:id>/', admin_views.delete_framework, name="delete_framework"),

    # component operations
    path('component-create/', admin_views.create_component, name="create_component"),
    path('component-update/<int:id>/', admin_views.update_component, name="update_component"),
    path('component-delete/<int:id>/', admin_views.delete_component, name="delete_component"),

    # focus operations
    path('focus-create/', admin_views.create_focus, name="create_focus"),
    path('focus-update/<int:id>/', admin_views.update_focus, name="update_focus"),
    path('focus-delete/<int:id>/', admin_views.delete_focus, name="delete_focus"),

    # algorithm operations
    path('algorithm-create/', admin_views.create_algorithm, name="create_algorithm"),
    path('algorithm-update/<int:id>/', admin_views.update_algorithm, name="update_algorithm"),
    path('algorithm-delete/<int:id>/', admin_views.delete_algorithm, name="delete_algorithm"),
]
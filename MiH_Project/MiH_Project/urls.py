from authentication import views as authentication_views
from projects_app import views as project_views
from admin_app import views as admin_views
from feedback_app import views as feedback_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [

    ##authentication routes
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="login.html")),
    path("register/", authentication_views.register, name="register"),
    path("signout/", authentication_views.signout, name="signout"),
    path("signin/", authentication_views.signin, name="signin"),
    path("user-homepage/", authentication_views.user_homepage, name="user_homepage"),
    path("profile/", authentication_views.profile_page, name="profile_page"),
    path("update-profile/<int:id>/", authentication_views.update_profile, name="update_profile"),
    path("change-password/", authentication_views.change_password, name="change_password"),

    # project_app routes
    path("sw-create/", project_views.create_software, name="sw_create"),
    path("hw-create/", project_views.create_hardware, name="hw_create"),
    path("ai-create/", project_views.create_ai, name="ai_create"),

    path('project-detail/<int:id>/', project_views.project_detail, name="project_detail"),
    path('project-search/', authentication_views.user_homepage, name="search_project"),

    path('sw-update/<int:id>', project_views.update_software, name="sw_update"),
    path('hw-update/<int:id>', project_views.update_hardware, name="hw_update"),
    path('ai-update/<int:id>', project_views.update_ai, name="ai_update"),

    path('project-delete/<int:id>/', project_views.project_delete, name="project_delete"),

    # admin routes
    path("user-list/", authentication_views.user_list, name="user_list"),
    path("project-list/", admin_views.project_list, name="project_list"),
    path("project-stats/", admin_views.project_stats, name="project_stats"),
    path('grant-admin/<int:id>/', admin_views.grant_admin, name="grant_admin"),
    path('revoke-admin/<int:id>/', admin_views.revoke_admin, name="revoke_admin"),

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

    #test pages
    path('new-dash/', TemplateView.as_view(template_name="admin-master.html"), name="dashboard"),
    path('new-stats/', TemplateView.as_view(template_name="multi.html"), name="new_stats"),

    # feedback_app routes
    path('add-comment/<int:project_id>/', feedback_views.add_comment, name="add_comment"),
    path('comment/delete/<int:comment_id>/', feedback_views.delete_comment, name='delete_comment'),
    path('add-rating/<int:project_id>/', feedback_views.add_rating, name="add_rating"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

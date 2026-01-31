from authentication import views as authentication_views
from projects_app import views as project_views

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
    path("test-homepage/", authentication_views.test_homepage, name="test_homepage"),
    path("profile/", authentication_views.profile_page, name="profile_page"),
    path("update-profile/<int:id>/", authentication_views.update_profile, name="update_profile"),
    path("change-password/", authentication_views.change_password, name="change_password"),

    #project_app routes
    path("sw-create/", project_views.create_software, name="sw_create"),
    path("hw-create/", project_views.create_hardware, name="hw_create"),
    path("ai-create/", project_views.create_ai, name="ai_create"),
    path('project-detail/<int:id>/', project_views.project_detail, name="project_detail"),
    path('project-update/<int:id>/', project_views.project_update, name="project_update"),
    path('project-delete/<int:id>/', project_views.project_delete, name="project_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

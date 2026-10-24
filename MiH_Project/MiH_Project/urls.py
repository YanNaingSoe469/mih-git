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


    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="login.html")),

    ##authentication routes
    path("auth/", include('authentication.urls')),

    # project_app routes
    path("project/", include('projects_app.urls')),

    # admin routes
    path("mih-admin/", include('admin_app.urls')),

    # feedback_app routes
    path("feedback/", include('feedback_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from authentication import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [

    ##authentication routes
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="login.html")),
    path("register/", views.register, name="register"),
    path("signout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
    path("test-homepage/", views.test_homepage, name="test_homepage"),
    path("profile/", views.profile_page, name="profile_page"),
    path("update-profile/<int:id>/", views.update_profile, name="update_profile"),
    path("change-password/", views.change_password, name="change_password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

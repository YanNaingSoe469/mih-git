from authentication import views as authentication_views
from projects_app import views as project_views
from admin_app import views as admin_views
from feedback_app import views as feedback_views

from django.urls import path

urlpatterns = [
path("register/", authentication_views.register, name="register"),
    path("signout/", authentication_views.signout, name="signout"),
    path("signin/", authentication_views.signin, name="signin"),
    path("user-homepage/", authentication_views.user_homepage, name="user_homepage"),
    path("profile/", authentication_views.profile_page, name="profile_page"),
    path("update-profile/<int:id>/", authentication_views.update_profile, name="update_profile"),
    path("change-password/", authentication_views.change_password, name="change_password"),
    path('announcements/', authentication_views.    announcement_list, name="announcement_list"),
]
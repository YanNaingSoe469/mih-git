from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page),
    path('login-page/', views.login_page, name='login#page'),
    path('register-page/', views.register_page, name='register#page'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('test-homepage/', views.test_homepage, name='test_homepage'),
    path('profile/', views.profilePage, name='profile_page'),
    path('update-profile/<int:id>/', views.updateProfile, name='update_profile'),
    path('change-password/<int:id>/', views.changePassword, name='change_password'),
]

import os

from django.apps import apps
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm, LoginForm
from .forms import UpdateProfileForm, ChangePasswordForm
from .models import *
from admin_app.models import Announcement


# from .projects_app.models import Language, Framework, Focus, Algorithm


# F1: Signup
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = "user"
            user.save()
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            return redirect("user_homepage")
        else:
            return render(request, "sign-up.html", {"form": form})
    else:
        form = RegistrationForm()
        return render(request, "sign-up.html", {"form": form})


# Logout
def signout(request):
    logout(request)
    return redirect("signin")


# F2: Login
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'admin' or user.role == 'rootadmin':
                return redirect('project_stats')
            else:
                return redirect('user_homepage')
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


# Direct to user homepage
def user_homepage(request):
    user = request.user

    key = request.GET.get('key', '')
    language = request.GET.get('language', '')
    framework = request.GET.get('framework', '')
    platform = request.GET.get('platform', '')

    level = request.GET.get('level', '')

    focus = request.GET.get('focus', '')
    algorithm = request.GET.get('algorithm', '')

    Project = apps.get_model('projects_app', 'Project')
    Software = apps.get_model('projects_app', 'Software')
    Hardware = apps.get_model('projects_app', 'Hardware')
    Ai = apps.get_model('projects_app', 'Ai')

    Language = apps.get_model('projects_app', 'Language')
    Framework = apps.get_model('projects_app', 'Framework')
    Focus = apps.get_model('projects_app', 'Focus')
    Algorithm = apps.get_model('projects_app', 'Algorithm')

    #software filtering
    if platform:
        projects = Software.objects.filter(platform=platform)
    elif language:
        projects = Software.objects.filter(language=language)
    elif framework:
        projects = Software.objects.filter(framework=framework)

    #hardware filtering
    elif level:
        projects = Hardware.objects.filter(skill_level=level)

    #ai filtering
    elif focus:
        projects = Ai.objects.filter(focus=focus)
    elif algorithm:
        projects = Ai.objects.filter(algorithms=algorithm)

    #searching
    elif key:
        projects = Project.objects.filter(title__icontains=key)
    else:
        projects = Project.objects.all()

    languages = Language.objects.all()
    frameworks = Framework.objects.all()
    focuses = Focus.objects.all()
    algorithms = Algorithm.objects.all()
    return render(request, "user_homepage.html",
                  {
                    "user": user,
                    'projects': projects,
                      'languages': languages,
                      'frameworks': frameworks,
                      'focuses': focuses,
                      'algorithms': algorithms,
                   }
                  )


#Direct to user management page
def user_list(request):
    key = request.GET.get('key', '')
    role = request.GET.get('role', '')

    if key:
        users = User.objects.filter(
            Q(name__icontains=key) | Q(email__icontains=key)
        ).order_by('name')
    elif role:
        users = User.objects.filter(role=role).order_by('name')
    else:
        users = User.objects.all().order_by('name')
    return render(request, "user-management.html", {'users': users})


# F3: View Profile
def profile_page(request):
    user = request.user
    if user.role == 'user':
        Project = apps.get_model('projects_app', 'Project')
        projects = Project.objects.filter(innovator_id=user.id)
        return render(request, "user-profile.html", {"user": user, 'projects': projects})
    else:
        return render(request, "admin_profile.html", {"user": user})


# F4: Update Profile
def update_profile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)

        #old profile path if exists
        old_profile_path = user.profile_pic.path if user.profile_pic.name and user.profile_pic.name != 'profile_pics/default-profile.png' else None

        if form.is_valid():
            #if the user uploads new profile
            if 'profile_pic' in request.FILES:

                #and the user already have an old profile
                if old_profile_path and os.path.isfile(old_profile_path):
                    os.remove(old_profile_path)

            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("update_profile", id=user.id)
    else:
        form = UpdateProfileForm(instance=user)
        if user.role == 'user':
            return render(request, "user-profile-update.html", {"form": form, "user": user})
        else:
            return render(request, "admin-profile-update.html", {"form": form, "user": user})


# F5: Change Password
def change_password(request):
    user = request.user
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated successfully!")
            return redirect("change_password")
    else:
        form = ChangePasswordForm(user=request.user)
        if user.role == 'user':
            return render(request, "user-change-password.html", {"form": form})
        else:
            return render(request, "admin-change-password.html", {"form": form})

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-date_time')
    return render(request, 'announcements.html', {"announcements": announcements})
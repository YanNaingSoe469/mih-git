from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm, LoginForm
from .forms import UpdateProfileForm, ChangePasswordForm
from .models import *


# Create your views here.
def login_page(request):
    return render(request, "login.html")


def register_page(request):
    return render(request, "sign-up.html")


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
            return redirect("test_homepage")
        else:
            return render(request, "sign-up.html", {"form": form})
    else:
        form = RegistrationForm()
        return render(request, "sign-up.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("login#page")


# def signin(request):
#     email = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, email=email, password=password)
#     if user:
#         login(request, user)
#         return redirect('test_homepage')
#     else:
#         return render(request, 'login-old.html')


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("test_homepage")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def test_homepage(request):
    user = request.user
    return render(request, "test_homepage.html", {"user": user})


def profilePage(request):
    user = request.user
    return render(request, "profile.html", {"user": user})


# def updateProfile(request, id):
#     data = User.objects.get(id=id)
#     if request.method == "POST":
#         profile_data = UpdateProfileForm(request.POST, instance=data)
#         if profile_data.is_valid():
#             profile_data.save()
#             return redirect("profile_page")
#         else:
#             messages.warning(request, "Could not update the data.")
#             return render(request, "profile-update.html", {"form": profile_data})
#     else:
#         form = UpdateProfileForm(instance=data)
#         return render(request, "profile-update.html", {"form": form})


def updateProfile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("update_profile", id=user.id)
    else:
        form = UpdateProfileForm(instance=user)

    return render(request, "profile-update.html", {"form": form, "user": user})


def changePassword(request):
    user = request.user

    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data["old_password"]
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if not user.check_password(old_password):
                messages.error(request, "Old password is incorrect")
            if old_password == new_password:
                messages.error(request, "Old password and new password are same")
            elif new_password != confirm_password:
                messages.error(
                    request, "New password and confirm password do not match"
                )
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password updated successfully!")
                return redirect("change_password")
    else:
        form = ChangePasswordForm()

    return render(request, "change-password.html", {"form": form})

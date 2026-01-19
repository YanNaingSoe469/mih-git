from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm, LoginForm
from .forms import UpdateProfileForm, ChangePasswordForm
from .models import *


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
            return redirect("test_homepage")
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
            return redirect("test_homepage")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


# Direct to homepage (Test)
def test_homepage(request):
    user = request.user
    return render(request, "test_homepage.html", {"user": user})


# F3: View Profile
def profile_page(request):
    user = request.user
    return render(request, "profile.html", {"user": user})


# F4: Update Profile
def update_profile(request, id):
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

    return render(request, "change-password.html", {"form": form})

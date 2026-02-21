import os
from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from projects_app.forms import ProjectCreateForm, SoftwareCreateForm, HardwareCreateForm, AiCreateForm

from projects_app.models import Project

from projects_app.models import Software, Hardware, Ai

from feedback_app.forms import CommentForm, RatingForm


# F7.1 Create Project (Software)
def create_software(request):
    if request.method == "POST":
        form = SoftwareCreateForm(request.POST, request.FILES)
        if form.is_valid():
            software = form.save(commit=False)
            software.innovator = request.user
            software.save()
            return redirect('user_homepage')
        else:
            return render(request, 'sw-create.html', {'form': form})
    else:
        form = SoftwareCreateForm()
        return render(request, 'sw-create.html', {'form': form})


# F7.1 Create Project (Hardware)
def create_hardware(request):
    if request.method == "POST":
        form = HardwareCreateForm(request.POST, request.FILES)
        if form.is_valid():
            hardware = form.save(commit=False)
            hardware.innovator = request.user
            hardware.save()
            form.save_m2m()
            return redirect('user_homepage')
        else:
            print(form.errors)
            return render(request, 'hw_create.html', {'form': form})
    else:
        form = HardwareCreateForm()
        return render(request, 'hw_create.html', {'form': form})


# F7.1 Create Project (AI)
def create_ai(request):
    if request.method == "POST":
        form = AiCreateForm(request.POST, request.FILES)
        if form.is_valid():
            ai = form.save(commit=False)
            ai.innovator = request.user
            ai.save()
            form.save_m2m()
            return redirect('user_homepage')
        else:
            print(form.errors)
            return render(request, 'ai_create.html', {'form': form})
    else:
        form = AiCreateForm()
        return render(request, 'ai_create.html', {'form': form})


# View project detail
def project_detail(request, id):
    user = request.user
    project_id = id
    if request.method == "GET":
        project = Project.objects.get(id=project_id)

        if project.type == "SW":
            project = Software.objects.get(id=project_id)
        elif project.type == "HW":
            project = Hardware.objects.get(id=project_id)
        else:
            project = Ai.objects.get(id=project_id)

        comments = project.comments.all()

        average_rating = project.ratings.aggregate(
            Avg("count")
        )["count__avg"]

        rounded_rating = round(average_rating) if average_rating else 0

        rating_count = project.ratings.aggregate(
            Count("id")
        )["id__count"]

        user_rating = None
        if request.user.is_authenticated:
            user_rating = project.ratings.filter(user=request.user).first()

        context = {
            "project": project,
            "comments": comments,
            "comment_form": CommentForm(),
            "rating_form": RatingForm(instance=user_rating),
            "average_rating": average_rating,
            "rounded_rating": rounded_rating,
            "rating_count": rating_count,
            "user_rating": user_rating,
        }

        if user.role == 'user':
            return render(request, 'user-project-detail.html', context)
        else:
            return render(request, 'admin-project-detail.html', context)
    return redirect('user_homepage')


# F7.3 Delete Project
def project_delete(request, id):
    project = Project.objects.get(id=id)
    cover_photo_path = project.cover_photo.path
    os.remove(cover_photo_path)
    project.delete()
    return redirect('profile_page')


# F6.1 Search Project
def search_project(request):
    search_key = request.GET.get('key')
    projects = Project.objects.filter(title__contains=search_key)
    return render(request, 'user_homepage.html', {'projects': projects})


# F7.2 Update Project (Software)
def update_software(request, id):
    software = Software.objects.get(id=id)

    if request.method == 'POST':
        form = SoftwareCreateForm(request.POST, request.FILES, instance=software)

        old_cover_photo_path = software.cover_photo.path
        if form.is_valid():
            if 'cover_photo' in request.FILES:
                os.remove(old_cover_photo_path)
            form.save()
            return redirect('project_detail', software.id)
        else:
            print(form.errors)
            if request.user.role == 'user':
                return render(request, 'user-sw-update.html', {'form': form})
            else:
                return render(request, 'admin-sw-update.html', {'form': form})
    else:
        form = SoftwareCreateForm(instance=software)
        if request.user.role == 'user':
            return render(request, 'user-sw-update.html', {'form': form})
        else:
            return render(request, 'admin-sw-update.html', {'form': form})


# F7.2 Update Project (Hardware)
def update_hardware(request, id):
    hardware = Hardware.objects.get(id=id)

    if request.method == 'POST':
        form = HardwareCreateForm(request.POST, request.FILES, instance=hardware)

        old_cover_photo_path = hardware.cover_photo.path
        if form.is_valid():
            if 'cover_photo' in request.FILES:
                os.remove(old_cover_photo_path)
            form.save()
            return redirect('project_detail', hardware.id)
        else:
            print(form.errors)
            if request.user.role == 'user':
                return render(request, 'user-hw-update.html', {'form': form})
            else:
                return render(request, 'admin-hw-update.html', {'form': form})
    else:
        form = HardwareCreateForm(instance=hardware)
        if request.user.role == 'user':
            return render(request, 'user-hw-update.html', {'form': form})
        else:
            return render(request, 'admin-hw-update.html', {'form': form})


# F7.2 Update Project (AI)
def update_ai(request, id):
    ai = Ai.objects.get(id=id)

    if request.method == 'POST':
        form = AiCreateForm(request.POST, request.FILES, instance=ai)

        old_cover_photo_path = ai.cover_photo.path
        if form.is_valid():
            if 'cover_photo' in request.FILES:
                os.remove(old_cover_photo_path)
            form.save()
            return redirect('project_detail', ai.id)
        else:
            print(form.errors)
            if request.user.role == 'user':
                return render(request, 'user-ai-update.html', {'form': form})
            else:
                return render(request, 'admin-ai-update.html', {'form': form})
    else:
        form = AiCreateForm(instance=ai)
        if request.user.role == 'user':
            return render(request, 'user-ai-update.html', {'form': form})
        else:
            return render(request, 'admin-ai-update.html', {'form': form})

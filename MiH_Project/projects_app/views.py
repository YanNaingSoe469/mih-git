import os
from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from projects_app.forms import ProjectCreateForm, SoftwareCreateForm, HardwareCreateForm, AiCreateForm

from projects_app.models import Project

from projects_app.models import Software, Hardware, Ai


# Create your views here.
def create_software(request):
    if request.method == "POST":
        form = SoftwareCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_homepage')
        return redirect('sw_create')
    else:
        form = SoftwareCreateForm()
        return render(request, 'sw-create.html', {'form': form})


def create_hardware(request):
    if request.method == "POST":
        form = HardwareCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_homepage')
        return redirect('hw_create')
    else:
        form = HardwareCreateForm()
        return render(request, 'hw-create.html', {'form': form})


def create_ai(request):
    if request.method == "POST":
        form = AiCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_homepage')
        return redirect('ai_create')
    else:
        form = AiCreateForm()
        return render(request, 'ai-create.html', {'form': form})


def project_detail(request, id):
    project_id = id
    if request.method == "GET":
        project = Project.objects.get(id=project_id)

        if project.type == "SW":
            project = Software.objects.get(id=project_id)
        elif project.type == "HW":
            project = Hardware.objects.get(id=project_id)
        elif project.type == "AI":
            project = Ai.objects.get(id=project_id)

        return render(request, 'project-detail.html', {'project': project})
    return redirect('test_homepage')


def project_update(request, id):
    project_id = id
    base = Project.objects.get(id=id)

    if base.type == "SW":
        project = Software.objects.get(id=id)
        FormClass = SoftwareCreateForm
    elif base.type == "HW":
        project = Hardware.objects.get(id=id)
        FormClass = HardwareCreateForm
    else:
        project = Ai.objects.get(id=id)
        FormClass = AiCreateForm


    if request.method == "POST":
        form = FormClass(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id)
        else:
            return render(request, 'project-update.html', {'form': form})
    else:
        form = FormClass(instance=project)
        print(form.errors)
        return render(request, 'project-update.html', {'form': form})


def project_delete(request, id):
    project = Project.objects.get(id=id)
    cover_photo_path = project.cover_photo.path
    os.remove(cover_photo_path)
    project.delete()
    return redirect('profile_page')
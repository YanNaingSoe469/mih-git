from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from projects_app.models import Project, Software, Hardware, Ai, Language, Framework, Component, Focus, Algorithm
from authentication.models import User
from admin_app.forms import CreateLanguageForm, CreateFrameworkForm, CreateComponentForm, CreateFocusForm, CreateAlgorithmForm, CreateAnnouncementForm, CreateContactForm
from admin_app.models import Announcement, Contact

CreateContactForm

def admin_required(view_func):
    return user_passes_test(lambda u: u.role == 'admin' or u.role == 'rootadmin')(view_func)

def rootadmin_required(view_func):
    return user_passes_test(lambda u: u.role == 'rootadmin')(view_func)


#Project Listing
@login_required
@admin_required
def project_list(request):
    key = request.GET.get('key', '')
    type = request.GET.get('type', '')
    if key:
        projects = Project.objects.filter(
            Q(title__icontains=key) | Q(innovator__name__icontains=key)
        ).order_by('-created_at')
    elif type:
        projects = Project.objects.filter(type=type).order_by('-created_at')
    else:
        projects = Project.objects.all().order_by('-created_at')
    return render(request, "project-list.html", {'projects': projects})


#Project Statistics
@login_required
@admin_required
def project_stats(request):
    project_count = Project.objects.all().count()
    sw_count = Software.objects.all().count()
    hw_count = Hardware.objects.all().count()
    ai_count = Ai.objects.all().count()
    return render(request, 'project-stats.html',
                  {
                      'project_count': project_count,
                      'sw_count': sw_count,
                      'hw_count': hw_count,
                      'ai_count': ai_count
                  }
                  )

#F10.1 Grant Admin
@login_required
@rootadmin_required
def grant_admin(request, id):
    user = User.objects.get(id=id)
    user.role = 'admin'
    user.save()
    return redirect('user_list')


#F10.2 Revoke Admin
@login_required
@rootadmin_required
def revoke_admin(request, id):
    admin = User.objects.get(id=id)
    admin.role = 'user'
    admin.save()
    return redirect('user_list')


#F11: Reference Data Management (language)
@login_required
@admin_required
def create_language(request):
    if request.method == 'POST':
        form = CreateLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_language')
        else:
            languages = Language.objects.all().order_by('name')
            return render(request, 'language-list.html', {'languages': languages, 'form': form})
    else:
        languages = Language.objects.all().order_by('name')
        form = CreateLanguageForm()
        return render(request, 'language-list.html', {'languages': languages, 'form': form})


#F11: Reference Data Management (language)
@login_required
@admin_required
def update_language(request, id):
    language = Language.objects.get(id=id)
    language.name = request.POST['name']
    language.save()
    return redirect('create_language')


@login_required
@admin_required
def delete_language(request, id):
    language = Language.objects.get(id=id)
    language.delete()
    return redirect('create_language')


@login_required
@admin_required
def create_framework(request):
    if request.method == 'POST':
        form = CreateFrameworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_framework')
        else:
            frameworks = Framework.objects.all().order_by('name')
            return render(request, 'framework-list.html', {'frameworks': frameworks, 'form': form})
    else:
        frameworks = Framework.objects.all().order_by('name')
        form = CreateLanguageForm()
        return render(request, 'framework-list.html', {'frameworks': frameworks, 'form': form})


@login_required
@admin_required
def update_framework(request, id):
    framework = Framework.objects.get(id=id)
    framework.name = request.POST['name']
    framework.save()
    return redirect('create_framework')

@login_required
@admin_required
def delete_framework(request, id):
    framework = Framework.objects.get(id=id)
    framework.delete()
    return redirect('create_framework')


@login_required
@admin_required
def create_component(request):
    if request.method == 'POST':
        form = CreateComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_component')
        else:
            components = Component.objects.all().order_by('name')
            return render(request, 'component-list.html', {'components': components, 'form': form})
    else:
        components = Component.objects.all().order_by('name')
        form = CreateComponentForm()
        return render(request, 'component-list.html', {'components': components, 'form': form})


@login_required
@admin_required
def update_component(request, id):
    component = Component.objects.get(id=id)
    component.name = request.POST['name']
    component.save()
    return redirect('create_component')


@login_required
@admin_required
def delete_component(request, id):
    component = Component.objects.get(id=id)
    component.delete()
    return redirect('create_component')


@login_required
@admin_required
def create_focus(request):
    if request.method == 'POST':
        form = CreateFocusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_focus')
        else:
            focuses = Focus.objects.all().order_by('name')
            return render(request, 'focus-list.html', {'focuses': focuses, 'form': form})
    else:
        focuses = Focus.objects.all().order_by('name')
        form = CreateComponentForm()
        return render(request, 'focus-list.html', {'focuses': focuses, 'form': form})


@login_required
@admin_required
def update_focus(request, id):
    focus = Focus.objects.get(id=id)
    focus.name = request.POST['name']
    focus.save()
    return redirect('create_focus')


@login_required
@admin_required
def delete_focus(request, id):
    focus = Focus.objects.get(id=id)
    focus.delete()
    return redirect('create_focus')


@login_required
@admin_required
def create_algorithm(request):
    if request.method == 'POST':
        form = CreateAlgorithmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_algorithm')
        else:
            algorithms = Algorithm.objects.all().order_by('name')
            return render(request, 'algorithm-list.html', {'algorithms': algorithms, 'form': form})
    else:
        form = CreateComponentForm()
        algorithms = Algorithm.objects.all().order_by('name')
        return render(request, 'algorithm-list.html', {'algorithms': algorithms, 'form': form})


@login_required
@admin_required
def update_algorithm(request, id):
    algorithm = Algorithm.objects.get(id=id)
    algorithm.name = request.POST['name']
    algorithm.save()
    return redirect('create_algorithm')


@login_required
@admin_required
def delete_algorithm(request, id):
    algorithm = Algorithm.objects.get(id=id)
    algorithm.delete()
    return redirect('create_algorithm')


#F12: Announcement Making
@login_required
@admin_required
def create_announcement(request):
    announcements = Announcement.objects.all().order_by('-date_time')
    if request.method == 'POST':
        form = CreateAnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_announcement')
        else:
            form = CreateAnnouncementForm()
            return redirect(request, 'announcement-list.html', {'form': form, 'announcements': announcements})
    else:
        form = CreateAnnouncementForm()
        return render(request, 'announcement-list.html', {'form': form, 'announcements': announcements})


#delete announcement
@login_required
@admin_required
def delete_announcement(request, id):
    announcement = Announcement.objects.get(id=id)
    announcement.delete()
    return redirect('create_announcement')

#update announcement
@login_required
@admin_required
def update_announcement(request, id):
    announcement = Announcement.objects.get(id=id)
    announcement.title = request.POST['title']
    announcement.message = request.POST['message']
    announcement.save()
    return redirect('create_announcement')

#F13: Contact Admin
@login_required
@admin_required
def create_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sent successfully.")
            return redirect('user_homepage')
    else:
        return redirect('user_homepage')

#Contact list
@login_required
@admin_required
def contact_list(request):
    contacts = Contact.objects.all().order_by('-date_time')
    return render(request, 'contact-list.html', {'contacts': contacts})
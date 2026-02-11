from django.shortcuts import get_object_or_404, redirect
from projects_app.models import Project

from .forms import CommentForm, RatingForm
from .models import Rating, Comment


# F8 Add Comment
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()

    return redirect("project_detail", id=project.id)


# F8 Delete Comment
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user:
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', 'test_homepage'))


# F9 Add Rating
def add_rating(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data["count"]

            rating, created = Rating.objects.update_or_create(
                project=project,
                user=request.user,
                defaults={"count": rating_value}
            )

    return redirect("project_detail", id=project.id)

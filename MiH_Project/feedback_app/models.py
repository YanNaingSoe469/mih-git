from django.conf import settings
from django.db import models
from projects_app.models import Project


class Comment(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comments"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.name} - {self.project.title}"


class Rating(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_ratings"
    )
    count = models.IntegerField()  # 1–5 stars

    class Meta:
        unique_together = ("project", "user")

    def __str__(self):
        return f"{self.project.title} - {self.count}"

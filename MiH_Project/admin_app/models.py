from django.db import models
from authentication.models import User


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Announcements"
    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Contacts"
    def __str__(self):
        return self.title
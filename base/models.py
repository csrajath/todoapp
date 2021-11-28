from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Task(models.Model):
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=254, null=True, blank=True)
    task_desc = models.TextField(null=True, blank=True)
    task_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title

    class Meta:
        order_with_respect_to = 'task_status'


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

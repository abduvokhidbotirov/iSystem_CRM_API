from django.db import models
from django.contrib.auth.models import User, Group

import user

STATUS = (
    (1, 'New'),
    (2, 'Process'),
    (3, 'Completed'),
)


class Planning(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.PositiveSmallIntegerField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)


class Task(models.Model):
    task_title = models.CharField(max_length=200, null=True) # not null
    task_description = models.CharField(max_length=200, blank=True)
    task_priority = models.PositiveSmallIntegerField(blank=True)
    task_status = models.IntegerField(choices=STATUS)
    task_deadline = models.DateField()
    task_done = models.BooleanField(default=False)
    task_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    task_created_at = models.DateField(auto_now=True)
    task_updated_at = models.DateTimeField(auto_now=True)


class Day(models.Model):
    date = models.DateField()
    daily_tasks = models.ManyToManyField(Task)


class SendTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sender = models.ForeignKey(user, on_delete=models.CASCADE)
    receiver = models.ForeignKey(user, on_delete=models.CASCADE, related_name='receiver_task', null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

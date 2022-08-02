from django.db import models

import user



class Notification(models.Model):
    title = models.CharField(max_length=222)
    description = models.TextField()
    user = models.ManyToManyField(user)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chat(models.Model):
    sender = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name='chat_sender')
    receiver = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name='chat_reciever')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


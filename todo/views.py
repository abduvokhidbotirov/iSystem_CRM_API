from django.db.models import Q
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from task.serializers import CommentSerializer
from .models import Reminder, Task, Comment, Project
from .serializers import (ReminderSerializer, TodoSerializer, ProjectSerializer)


class TodoView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
         qs = Task.objects.all()
         query = self.request.get('q')
         if query is not None:
             qs = qs.filter(Q(title__icontains=query) |
                            Q(description__icontains=query)
                            ).distinct()
         return qs



class ReminderView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class CommentView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
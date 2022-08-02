from django.utils import timezone
from rest_framework import serializers

from .models import Reminder, Task, Comment, Project


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Task
        fields = ('project', 'title', 'description',
                  'deadline', 'priority', 'reminders_ids')
        read_only_fields = ('reminders_ids',)



    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('kelgusidagi sanani tanlang.')
        return value


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Reminder
        fields = ('id', 'url', 'task', 'date')
        read_only_fields = ('id',)

    def validate_date(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('kelgusidagi sanani tanlang.')
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Comment
        fields = ('id', 'url', 'task', 'comment')
        read_only_fields = ('id',)
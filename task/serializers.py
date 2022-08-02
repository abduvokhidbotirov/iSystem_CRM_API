from rest_framework import serializers
from .models import Task, SendTask, Comment
from user.serializers import RegisterSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['task', 'user', 'message', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'task_priority', 'task_status', 'task_deadline', 'task_done', 'task_user', 'task_created_at', 'task_updated_at']


class CommentSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    task = TaskSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'message', 'created_at']


class SendTaskSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(max_length=222, read_only=True)

    class Meta:
        model = SendTask
        fields = ['task', 'sender', 'receiver', 'created_at']
        extra_kwargs = {
            'sender': {'required': False}
        }
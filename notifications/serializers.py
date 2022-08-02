from rest_framework import serializers
from .models import Notification, Chat
from user.serializers import RegisterSerializer


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'title',
            'description',
            'user',
            'created_at'
        ]


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'sender',
            'receiver',
            'message',
            'created_at',
            'updated_at',
        ]


class ChatListSerializer(serializers.ModelSerializer):
    sender = RegisterSerializer()
    receiver = RegisterSerializer()

    class Meta:
        model = Chat
        fields = [
            'sender',
            'receiver',
            'message',
            'created_at',
            'updated_at',
        ]
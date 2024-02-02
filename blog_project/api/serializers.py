from rest_framework import serializers

from blog import models
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'registration_date']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['id', 'user']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'blog', 'title', 'text', 'created_at', 'read']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ['id', 'subscriber', 'blog']

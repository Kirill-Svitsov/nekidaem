from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import Blog, Post, Subscription
from .serializers import (
    BlogSerializer,
    PostSerializer,
    SubscriptionSerializer,
    UserSerializer
)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=False,
        methods=['GET'],
        url_path='news'
    )
    def news_feed(self, request):
        user = self.request.user
        subscriptions = Subscription.objects.filter(subscriber=user)
        posts = Post.objects.filter(blog__in=subscriptions.values('blog')).order_by('-created_at')[:500]

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        blog = get_object_or_404(Blog, user=self.request.user)
        serializer.save(blog=blog)


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        serializer.save(subscriber=self.request.user)

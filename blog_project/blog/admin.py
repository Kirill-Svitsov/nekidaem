from django.contrib import admin
from .models import Blog, Post, Subscription


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('blog', 'title', 'created_at', 'read')
    list_filter = ('blog', 'created_at')
    search_fields = ('title', 'text')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'blog',)
    list_filter = ('subscriber', 'blog',)
    search_fields = ('subscriber__username', 'blog__user__username')

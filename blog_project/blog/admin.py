from django.contrib import admin
from .models import Blog, Post, Subscription


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author_username', 'title', 'created_at', 'read')
    list_display_links = ('blog', 'title')
    list_filter = ('blog', 'created_at')
    search_fields = ('title', 'text')

    def author_username(self, obj):
        return obj.blog.user.username


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'blog')
    list_display_links = ('subscriber', 'blog')
    list_filter = ('subscriber', 'blog')
    search_fields = ('subscriber__username', 'blog__user__username')

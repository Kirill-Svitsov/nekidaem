from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import Post, Subscription
from .models import User


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 1


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'first_name', 'last_name', 'registration_date']
    list_display_links = ['email', 'username', 'first_name', 'last_name', 'registration_date']
    search_fields = ['email', 'username']
    ordering = ['username']
    inlines = [PostInline, SubscriptionInline]

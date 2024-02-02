from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Blog
from users.models import User


@receiver(post_save, sender=User)
def create_user_blog(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(user=instance)


post_save.connect(create_user_blog, sender=User)

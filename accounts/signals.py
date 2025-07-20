from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance: UserModel, created: bool, **kwargs) -> None:
    if created:
        Profile.objects.create(nickname=instance)

from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.models import EmailAddress

from .models import User, Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        if instance.is_superuser:
            EmailAddress.objects.create(
                user=instance,
                email=instance.email,
                primary=True,
                verified=True,
            )

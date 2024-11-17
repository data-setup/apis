# profiles/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings  # لاستخدام AUTH_USER_MODEL
from .models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """
    إنشاء بروفايل بشكل تلقائي عند إنشاء مستخدم جديد.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    """
    حفظ البروفايل عند حفظ المستخدم.
    """
    instance.profile.save()

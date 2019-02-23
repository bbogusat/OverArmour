from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Adds profile model to the User - One to One


class Profile(models.Model):
    # Ensures profile is deleted when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    weight = models.CharField(max_length=30, blank=True)

    # On user creation create a profile
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # When user is saved also save profile
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

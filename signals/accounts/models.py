from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created')


post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created is False:
        Profile.objects.create(user=instance)
        print('Profie created for existing user')


post_save.connect(update_profile, sender=User)

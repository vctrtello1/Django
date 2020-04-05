from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Costumer


def costumer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='costumer')
        instance.groups.add(group)
        Costumer.objects.create(
            user=instance,
            name=instance.username,
            )
        instance.groups.add(group)
        Costumer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created')


post_save.connect(costumer_profile, sender=User)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        # create the profile of the user, yes! instance is the user (gangadhar hi shaktiman h!)
        owner_profile = Profile.objects.create(owner=instance)
        # add self profile in the following list. We're following our own profile so that we can see our posts
        # too, in addition to the followed profile's posts.
        owner_profile.following.add(instance.profile)





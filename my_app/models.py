from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # Each user will have exactly one profile or vice-versa
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    # A profile can follow multiple account and can be followed by multiple accounts at the same time, that's why
    # we've used M2M field. The related_name attribute specifies the name of the reverse relation.

    # here, self means that the model has an M2M relation with itself
    following = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.owner.username}'

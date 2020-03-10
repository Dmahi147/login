from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=30)
    email_confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.user.username


def update_user_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(update_user_profile, sender=User)

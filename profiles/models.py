from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(User):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

def create_or_update_user_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
    
post_save.connect(create_or_update_user_profile,sender=User)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid
# Create your models here.

class User(AbstractUser):
    # shifting all alternate authentication to user_profile model
    # phone_number = models.CharField(max_length=15, unique=True)
    # whatsapp_number = models.OneToOneField('UserProfile', on_delete=models.CASCADE, to_field='whatsapp_number', related_name='my_user', null=True)
    
    email = models.EmailField(unique=True)


    REQUIRED_FIELDS = ['first_name','last_name','username']
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD = 'whatsapp_number' #this leads to issues when creating admin
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
    
    def set_full_name(self, full_name):
        parts = full_name.strip().split()
        self.first_name = parts[0]
        self.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.URLField(max_length=200, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    # default=uuid.uuid4,
    def __str__(self):
        return f"{self.user.email} profile"
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True)
    intro = models.TextField(max_length=255, blank=True, null=True)
    profile = models.TextField(max_length=2000, blank=True, null=True)
    

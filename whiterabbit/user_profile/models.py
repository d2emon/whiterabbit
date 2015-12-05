from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    motto = models.CharField(max_length=255)

# Create your models here.

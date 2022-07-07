from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from model_utils.models import TimeStampedModel

from users.managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
  
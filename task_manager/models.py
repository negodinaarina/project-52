from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
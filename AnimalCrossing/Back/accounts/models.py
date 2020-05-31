from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(unique=True, max_length=255)
  username = None
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  def __str__(self):
    return self.email

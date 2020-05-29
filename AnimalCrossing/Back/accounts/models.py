from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(primary_key=True, unique=True, max_length=255)
  def __str__(self):
    return self.email

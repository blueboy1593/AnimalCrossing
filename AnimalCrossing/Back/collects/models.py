from django.db import models
from django.conf import settings

class Fish(models.Model):
    name = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    price = models.CharField(max_length=10)


class Insect(models.Model):
    name = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class Fossil(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class Painting(models.Model):
    # original 없애기
    name = models.CharField(max_length=20)
    real = models.CharField(max_length=50)
    original = models.CharField(max_length=50)
    engname = models.CharField(max_length=50)
    memo = models.CharField(max_length=20)

class Animal(models.Model):
    name = models.CharField(max_length=20)
    engname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=10)
    personality = models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
# Create your models here.

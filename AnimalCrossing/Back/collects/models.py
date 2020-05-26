from django.db import models
from django.conf import settings

class Fish(models.Model):
    fish_name = models.CharField(max_length=20)
    fish_month = models.CharField(max_length=20)
    fish_time = models.CharField(max_length=20)
    fish_size = models.CharField(max_length=10)
    fish_location = models.CharField(max_length=20)
    fish_price = models.CharField(max_length=10)


class Insect(models.Model):
    insect_name = models.CharField(max_length=20)
    insect_month = models.CharField(max_length=20)
    insect_time = models.CharField(max_length=20)
    insect_location = models.CharField(max_length=20)
    insect_price = models.CharField(max_length=10)

class Fossil(models.Model):
    fossil_name = models.CharField(max_length=20)
    fossil_price = models.CharField(max_length=10)

class Painting(models.Model):
    painting_name = models.CharField(max_length=20)
    painting_real = models.CharField(max_length=50)
    painting_original = models.CharField(max_length=50)
    painting_engname = models.CharField(max_length=50)
    painting_memo = models.CharField(max_length=20)

class Animal(models.Model):
    animal_name = models.CharField(max_length=20)
    animal_engname = models.CharField(max_length=20)
    animal_gender = models.CharField(max_length=10)
    animal_birthday = models.CharField(max_length=10)
    animal_personality = models.CharField(max_length=20)
    animal_sort = models.CharField(max_length=20)
# Create your models here.

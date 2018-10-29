from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
GENDER = (
	('M', 'MALE'),
	('F', 'FEMALE'),
	('N', 'NEUTRAL'),
	)


class Passenger(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10)
	#gender can be used to book cabs with female drivers for female passenger
	gender = models.CharField(max_length=1, choices=GENDER)


class Driver(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
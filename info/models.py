from django.contrib.auth.models import User
from django.db import models


class BloodInfo(models.Model):
    Male = 'Male'
    Female = 'Female'
    SEX_CHOICES = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

    BLOOD_GROUP_CHOICES = [
        (A_POSITIVE,'A+'),
        (A_NEGATIVE, 'A-'),
        (B_POSITIVE, 'B+'),
        (B_NEGATIVE, 'B-'),
        (AB_POSITIVE, 'AB+'),
        (AB_NEGATIVE, 'AB-'),
        (O_POSITIVE, 'O+'),
        (O_NEGATIVE, 'O-'),
    ]
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False, default=1)
    blood_group = models.CharField(max_length=10,
                                   choices=BLOOD_GROUP_CHOICES,
                                   default='')
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
        default=Male,
    )
    location = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.blood_group

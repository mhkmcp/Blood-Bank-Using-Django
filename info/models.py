from django.db import models


class UserInfo(models.Model):
    Male = 'M'
    Female = 'F'
    SEX_CHOICES = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
        default=Male,
    )
    location = models.TextField()

    def __str__(self):
        return self.first_name


class BloodRecord(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    blood_gorup = models.CharField(max_length=5)

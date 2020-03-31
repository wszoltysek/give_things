from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


TYPES = (
        (1, 'Fundacja'),
        (2, 'Organizacja pozarządowa'),
        (3, 'Zbiórka lokalna'),
    )


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ManyToManyField(Institution)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    phone_number = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Dar dla: {self.institution.name}"

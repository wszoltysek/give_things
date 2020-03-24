from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)


class Institution(models.Model):
    TYPES = (
        (1, 'Fundacja'),
        (2, 'Organizacja pozarządowa'),
        (3, 'Zbiórka lokalna'),
    )

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

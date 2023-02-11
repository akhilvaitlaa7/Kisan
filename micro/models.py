from django.db import models


class Calculation(models.Model):
    total_bags = models.PositiveIntegerField()
    weight_kgs = models.PositiveIntegerField()
    commission = models.PositiveIntegerField()
    labour_cost = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

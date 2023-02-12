from django.db import models


# from django.contrib.auth.models import User

class User(models.Model):
    name = models.TextField()


class Calculation(models.Model):
    total_bags = models.PositiveIntegerField()
    weight_kgs = models.PositiveIntegerField()
    commission = models.PositiveIntegerField()
    labour_cost = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    result = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)




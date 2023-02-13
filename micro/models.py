from django.db import models
import datetime


class User(models.Model):
    name = models.TextField()


class Calculation(models.Model):
    total_bags = models.PositiveIntegerField()
    weight_kgs = models.PositiveIntegerField()
    commission = models.PositiveIntegerField()
    labour_cost = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    result = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


def user_directory_path(instance, filename):
    return f'{instance.user.id}/{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_{filename}'


class ImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    timestamp = models.DateTimeField(auto_now_add=True)

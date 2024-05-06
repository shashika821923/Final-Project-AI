from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    height_cm = models.FloatField()
    weight_kg = models.FloatField()
    meal_plan = models.CharField(max_length=100)
    foods = models.TextField()

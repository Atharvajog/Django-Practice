from django.db import models

# Create your models here.
class car(models.Model):
    car_name=models.CharField(max_length=200)
    car_speed=models.IntegerField()

    def __str__(self) -> str:
        return self.car_name
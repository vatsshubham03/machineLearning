from django.db import models

# Create your models here.
from django.db import  models


class Position(models.Model):
    title = models.CharField(max_length=100)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

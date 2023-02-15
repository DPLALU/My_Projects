from django.db import models

# Create your models here.
class Employee(models.Model):
    Empname = models.CharField(max_length=20)
    Empid = models.IntegerField()
    Empemail = models.CharField(max_length=30)
    Empnumber = models.IntegerField()

from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpName = models.CharField(max_length=30)
    EmpSalary=models.IntegerField()
    EmpAddress=models.CharField(max_length=30)

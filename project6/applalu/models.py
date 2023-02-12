from django.db import models

# Create your models here.
class Mobile(models.Model):
    MobileName = models.CharField(max_length=20)
    MobilePrice = models.IntegerField()
    MobileModel = models.CharField(max_length=20)
    MobileColor = models.CharField(max_length=20)

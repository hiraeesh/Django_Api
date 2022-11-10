from django.db import models

# Create your models here.
class abc(models.Model):
    fieldName = models.CharField(max_length = 150)
    lname=models.CharField(max_length=40)
    

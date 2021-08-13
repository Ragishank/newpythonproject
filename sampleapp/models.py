from django.db import models

# Create your models here.

class student(models.Model):
    firstname=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    dob=models.DateField()
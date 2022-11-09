from django.db import models

# Create your models here.
class firstclass(models.Model):
    stuname=models.CharField(max_length=50)
    stusurname=models.CharField(max_length=50)
    stuage=models.IntegerField()
    sturoll_no=models.IntegerField()

class secondclass(models.Model):
    stuname=models.CharField(max_length=50)
    stusurname=models.CharField(max_length=50)
    stuage=models.IntegerField()
    sturoll_no=models.IntegerField()

class thirdclass(models.Model):
    stuname=models.CharField(max_length=50)
    stusurname=models.CharField(max_length=50)
    stuage=models.IntegerField()
    sturoll_no=models.IntegerField()

class fourthclass(models.Model):
    stuname=models.CharField(max_length=50)
    stusurname=models.CharField(max_length=50)
    stuage=models.IntegerField()
    sturoll_no=models.IntegerField()
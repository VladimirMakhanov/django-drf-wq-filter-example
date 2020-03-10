from django.db import models

# Create your models here.


class Model1(models.Model):
    param1 = models.IntegerField()


class Model2(models.Model):
    param2 = models.CharField(max_length=20)


class TestModel(models.Model):
    one = models.IntegerField()
    two = models.TextField()

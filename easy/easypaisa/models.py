from django.db import models
import datetime
# Create your models here.


class Income(models.Model):
    income = models.CharField(max_length=5)
    date_added = models.DateField(default=datetime.datetime.now, null=True)
    remark = models.CharField(max_length=100)


class Expenses(models.Model):
    price = models.CharField(max_length=5)
    date_added = models.DateField(default=datetime.datetime.now, null=True)
    category = models.CharField(max_length=10, default='Food')
    remark = models.CharField(max_length=100)


class Budget(models.Model):
    budget = models.CharField(max_length=5)
from django.db import models
from django.contrib.auth.models import User

import re
import os

TBL_NAME_LIST = [
    'Customer',
    'Membership',
    'Product',
    'Purchasing',
    'Expenditure',
]

class Customer(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=16)
    birthday = models.DateField()
    
    class Meta:
        unique_together = ('name', 'phone')

class Membership(models.Model):
    regDate = models.DateField(auto_now_add=True)
    balance = models.DecimalField(max_digits=19, decimal_places=2)
    passphrase = models.CharField(max_length=32)
    customerNo = models.ForeignKey(Customer, related_name='membership', null=True, on_delete=models.SET_NULL)

class Product(models.Model):
    name = models.CharField(max_length=32)
    count = models.BigIntegerField(null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    details = models.CharField(max_length=255)

class Purchasing(models.Model):
    productNo = models.ForeignKey(Product, related_name='pur_prod', null=True, on_delete=models.SET_NULL)
    membershipNo = models.ForeignKey(Membership, related_name='pur_member', null=True, on_delete=models.SET_NULL)
    count = models.BigIntegerField(null=True)
    payment = models.DecimalField(max_digits=19, decimal_places=2)
    dtime = models.DateTimeField(auto_now_add=True)
    
class Expenditure(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)
    payment = models.DecimalField(max_digits=19, decimal_places=2)
    details = models.CharField(max_length=255)
    productNo = models.ForeignKey(Product, related_name='buyingIn', blank=True, null=True, on_delete=models.SET_NULL)
    count = models.BigIntegerField(null=True) 
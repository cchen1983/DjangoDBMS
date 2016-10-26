# Data Models
# cchen @ 2016.09.02

from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

import re
import os

TBL_NAME_LIST = [
    'Customer',
    'Membership',
    'Product',
    'Purchasing',
    'Expenditure',
    'Discount',
    'Promotion',
]

class Customer(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=16)
    birthday = models.DateField()
    
    # cchen @ 2016.09.10:
    #   Add unique constraints for name+phone combination 
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

TGT_ALL = 'All'
TGT_MEMBER = 'Member'
TGT_BD = 'Birthday' 

#PROMO_N_GET_1 = 'PM_N1'     # Promotion Buy N get 1
#PROMO_DISCOUNT = 'PM_DC'    # Promotion Discount

# cchen @ 20161009
class Activity(models.Model):
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=255)
    target = models.CharField(max_length=32)

# Discount for all products 
class Discount(Activity):
    disc = models.DecimalField(max_digits=19, decimal_places=2)

    def save(self):
        Discount.objects.all().delete()
        super(Discount, self).save()
        
# Yihang Zhao @  20161011       
# Promotion for specific product
class Promotion(Activity):
    productNo = models.ForeignKey(Product, related_name='promotion', blank=True, null=True, on_delete=models.SET_NULL)
    n1 = models.BigIntegerField(null=True)
    #pmType = models.CharField(max_length=32) 
    #discount = models.DecimalField(max_digits=19, decimal_places=2, null=True)

    def save(self):
        try:
            try:
                self.productNo.promotion.get()
                print 'replace the promotion of ' + self.productNo.name
                self.productNo.promotion.clear() 
            except ObjectDoesNotExist:
                print 'place the promotion of ' + self.productNo.name
        except ObjectDoesNotExist:
            print 'specified product not exist.'

        super(Promotion, self).save()

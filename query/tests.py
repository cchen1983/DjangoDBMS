# Unittest for DataModel
# cchen @ 2016.11.23

import sys
import datetime

from django.test import TestCase
from query.models import *

class QueryTestCase(TestCase):
    def setUp(self):
        today = datetime.datetime.now().date()

        c1 = Customer(name="tony",phone="1234567890",address="address_tony",gender="Male", birthday=today)
        c2 = Customer(name="jamail",phone="2234567890",address="address_jamial",gender="Male", birthday=today)
        c3 = Customer(name="hanbing",phone="3234567890",address="address_hanbing",gender="Female", birthday=today)
        c1.save()
        c2.save()
        c3.save()

        m1 = Membership(balance=100, passphrase='pwd_tony', customerNo=c1)
        m2 = Membership(balance=100, passphrase='pwd_hanbing', customerNo=c3)
        m1.save()
        m2.save()        

    def test_membership_check(self):
        c1 = Customer.objects.get(name="tony")
        c2 = Customer.objects.get(name="jamail")
        c3 = Customer.objects.get(name="hanbing")

        self.assertTrue(len(Membership.objects.filter(customerNo=c1)) >= 1, msg="Customer1 is a member.")
        self.assertFalse(len(Membership.objects.filter(customerNo=c2)) >= 1, msg="Customer2 is not a member.")
        self.assertTrue(len(Membership.objects.filter(customerNo=c3)) >= 1, msg="Customer3 is a member.")


    def test_purchasing(self):
        p1 = Product.objects.create(name="coke", count=20, price=2.0, details="None")
        p2 = Product.objects.create(name="cupcake", count=20, price=3.0, details="None")
        p3 = Product.objects.create(name="chip", count=20, price=2.0, details="None")
        
        old = p1.count;
        p1.count = p1.count - 3
        payment = 6.0
        pur1 = Purchasing(productNo=p1, count=3, payment=payment)
        p1.save()
        pur1.save()

        self.assertEqual(payment, p1.price*3, msg="Payment of 3 cups of coke should be " + str(p1.price*3))
        self.assertEqual(p1.count, old - 3, msg="The count should be reduced by 3.")

        old = p2.count;
        p2.count = p2.count - 10
        payment = p2.price * 10
        pur2 = Purchasing(productNo=p2, count=10, payment=payment)
        p2.save()
        pur2.save()

        self.assertEqual(payment, p2.price*10, msg="Payment of 10 cupcakes should be " + str(p2.price*10))
        self.assertEqual(p2.count, old - 10, msg="The count should be reduced by 10.")


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

#from mysqlUtils import dbQuery

from query.models import *

import datetime
from decimal import Decimal

@login_required
def index(request):
    return render(request, 'workflow/index.html')

@login_required
def check_membership(request):
    membershipNo = request.POST.get('membershipNo')
    resp = ''
    try:
        res = Membership.objects.get(id=membershipNo)
        resp = res.balance
    except:
        resp = 'NotExist'

    return HttpResponse(resp)

@login_required
def reg_form_view(request):
    tp = request.GET.get('type')
    if tp == 'mem_new':
        return render(request, 'workflow/member_new.html')
    elif tp == 'mem_rec':
        return render(request, 'workflow/member_recharge.html')
    elif tp == 'exp_prod':
        products = Product.objects.all()
        return render(request, 'workflow/exp_product.html', {'products': products})
    elif tp == 'exp_other':
        return render(request, 'workflow/exp_other.html')
    elif tp == 'prc_new':
        products = Product.objects.all()
        return render(request, 'workflow/prc_new.html', {'products': products})

@login_required
def add_new_member(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    balance = request.POST.get('balance')
    passphrase = request.POST.get('passphrase')
    address = request.POST.get('address')
    
    resp = 'OK'

    try:
        cus = Customer(name=name, phone=phone, address=address, gender=gender, birthday=birthday)
        print cus, cus.name, cus.phone, cus.address, cus.gender, cus.birthday
        cus.save()
        print 'cus save ok.'
        mem = Membership(balance=balance, passphrase=passphrase, customerNo=cus)
        print mem
        mem.save() 
        print 'mem save ok'
    except:
        print >> sys.stderr, traceback.format_exc()
        resp = 'create member error'

    return HttpResponse(resp)

@login_required
def member_recharge(request):
    membershipNo = request.POST.get('membershipNo')
    balance = request.POST.get('balance')
    
    resp = 'OK'

    try:
        mem = Membership.objects.get(id=membershipNo)
        mem.balance = mem.balance + Decimal(balance)
        mem.save()
    except:
        print >> sys.stderr, traceback.format_exc()
        resp = 'recharge error'    

    return HttpResponse(resp)

@login_required
def exp_product_reg(request):
    resp = 'OK'
    needUpdate = True

    productNo = request.POST.get('product')
    count = request.POST.get('count')
    details = request.POST.get('details')
    print productNo, count, details
    try:
        if productNo == "new":
            new_name = request.POST.get('product_new')
            new_price= request.POST.get('product_price')
            prod = Product(name=new_name, price=new_price, count=count)
            prod.save()
            productNo = prod.id
            needUpdate = False

        payment = request.POST.get('payment')
        prod = Product.objects.get(id=productNo)
        exp = Expenditure(payment=payment, details=details, productNo=prod, count=count)
        exp.save()

        if needUpdate:
            prod.count = prod.count + long(count)
            prod.save()
        
    except:
        print >> sys.stderr, traceback.format_exc()
        resp = 'exp product reg error'

    return HttpResponse(resp)

@login_required
def exp_other_reg(request):
    resp = 'OK'

    payment = request.POST.get('payment')
    details = request.POST.get('details')
    
    try:
        exp = Expenditure(payment=payment, details=details)
        exp.save()
    except:
        print >> sys.stderr, traceback.format_exc()
        resp = 'exp other reg error'

    return HttpResponse(resp)

@login_required
def purc_reg(request):
    resp = 'OK'
    productNo = request.POST.get('product')
    price = Decimal(request.POST.get('price'))
    count = request.POST.get('count')
    membershipNo = request.POST.get('membershipNo')
    payment = Decimal(request.POST.get('payment'))
    balance = Decimal(0)
    mem = None

    if membershipNo:
        mem = Membership.objects.get(id=membershipNo)
        balance = mem.balance

    charge = price * int(count)
    bcharge = charge - payment

    if mem:
        mem.balance = balance - bcharge
        mem.save()

    prod = Product.objects.get(id=productNo)
    prod.count = prod.count - int(count) 
    prod.save()

    pur = Purchasing(productNo=prod, membershipNo=mem, count=count, payment=charge)
    pur.save()

    return HttpResponse(resp)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

#from mysqlUtils import dbQuery

def index(request):
    return render(request, 'contacts/index.html')

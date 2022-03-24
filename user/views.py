import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    return render(request,'reg.html')

def login(request):
    return render(request,'login.html')

def admin(request):
    return render(request,'admin.html')

def emp(request):
    return render(request,'emp.html')

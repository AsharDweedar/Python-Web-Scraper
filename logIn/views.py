from django.shortcuts import render, redirect
from django.conf.urls import include
from django.http import HttpResponse

import requests
import lxml.html

from .models import Users
from dashbord.models import Dashbord

def submit(request):
    data = request._get_request()
    print(data)
    print('name')
    print(data.get('name'))
    print('password')
    print(data.get('password'))

    if not Users.objects.filter(name=data.get('name'),password=data.get('password')):
        return render(request, "signIn.html", {})

    URLs_List = Dashbord.objects.all()
    print(len(URLs_List))
    context = {
        'URLs_List': URLs_List,
    }
    return render(request, 'index.html',context)

def signup(request):
    data = request._get_request()
    print('inside signup')
    print(dir(data))
    print('new_name')
    print(data.get('new_name'))
    print('password')
    print(data.get('new_password'))

    Users.objects.create(name=data.get('new_name'),password=data.get('new_password'))
    return render(request, "signIn.html", {})


def index(request):
    print('login/index')
    return render(request, "signIn.html", {})

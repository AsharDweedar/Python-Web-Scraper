from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import include

#db table
from .models import Dashbord

def index(request):
    return render(request, "dashbord.html", {})

def scraped(request):
    return HttpResponse("scraped end point with one argumant :( " )
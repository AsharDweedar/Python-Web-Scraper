#basics
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import include

# for scrapping
import requests
#import python-lxml


#db table
from .models import Dashbord

def index(request):
    return render(request, "dashbord.html", {something : "hi there"})

def scraped(request):
    return HttpResponse("scraped end point with one argumant :( " )

def runScrapper(request):
    requests()
    return HttpResponse("scraped end point with one argumant :( " )
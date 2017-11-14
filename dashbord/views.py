#basics
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import include

# for scrapping
import requests
import lxml.html
#import cssselect # import error 

#db table
from .models import Dashbord

def index(request):
    return render(request, "dashbord.html", {something : "hi there"})

def scraped(request):
    return HttpResponse("scraped end point with one argumant :( " )

def runScrapper(request):
    res = requests.get("http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=coursez")
    # print(res.text)
    # treeObj = lxml.html.HTML(res.text)
    treeObj = lxml.html.fromstring(res.text)
    someTag = treeObj.xpath("//div[@id='mh_course_menu']") # title as example => it doesn't work 
    print("someTag : ")
    print(someTag.text.strip())
    print("....................................................................")
    return HttpResponse("run scrapper end point :( " )
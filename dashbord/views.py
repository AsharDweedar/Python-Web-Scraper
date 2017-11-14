#basics
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import include

# for scrapping
import requests
import lxml.html
from lxml.html import etree
#import cssselect # import error 

#db table
from .models import Dashbord

def runScrapper(request):
    res = requests.get("http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=coursez")

    treeObj = lxml.html.fromstring(res.text)
    container = treeObj.xpath("//div[@id='mh_course_menu']")
    chapters = container[0].xpath('.//div')
    for unitsContainer in chapters:
        unitsDiv = unitsContainer.xpath('.//div')
        if (len(unitsDiv) > 0):
            unitsDiv = unitsDiv[0]
            units = unitsDiv.xpath('.//p')
            print('%s units : ' % len(units))
            for unit in units:
                link = "http://www.mathhelp.com/{}".format(unit.xpath('.//a/@href')[0])
                print('link : {}'.format(link))
                scrappURL(link)                
    print("....................................................................")
    return HttpResponse("run scrapper end point , done scrapping " )

def scrappURL(link):
    all = requests.get(link)
    treeObj = lxml.html.fromstring(all.text)
    title = treeObj.xpath("//div[@id='mh_lesson_page']")[0].xpath('.//h1')[0]
    content = treeObj.xpath("//div[@id='mh_lesson_page']")[0].xpath('.//p')[0]
    title = etree.tostring(title,with_tail=False)[4:-5]
    content = etree.tostring(content,with_tail=False)[3:-4]
    print(title)
    if not Dashbord.objects.filter(title=title):
        print('%s saved' %title)
        row = Dashbord.objects.create(title=title,content=content,url=link)


    
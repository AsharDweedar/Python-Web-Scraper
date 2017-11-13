from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^scraped/', views.scraped, name='scraped'),
    url(r'^runScrapper/', views.runScrapper, name='scraped'),
]
    # url(r'(?P<title>[a-z])/scraped$', views.scraped, name='scraped'),

'''
$   : the thing before it at the end 
^   : the thing after it at the begining
()  : remember this match
[]  : match whats inside letterly
[^x]: don't match 'x'

'''
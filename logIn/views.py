from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Users
from dashbord.models import Dashbord

def submit(request):#, name, password):
    print('name')
    print(request) 
    # URLs_List = Dashbord.objects
    URLs_List = [{"title": "title1"},{"title": "title2"},{"title": "title3"},] #Dashbord.objects
    print(URLs_List)
    context = {
        'URLs_List': URLs_List,
    }
    return render(request, 'list.html',context)


def index(request):
    print('login/index')
    return render(request, "signIn.html", {})

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Users
from dashbord.models import Dashbord

def submit(request):#, name, password):
    data = request._get_request()
    user = {
        "name" : data.get('name'),
        "password" : data.get('password'),
    }
    print(dir(data))
    print('name')
    print(data.get('name'))
    print('password')
    print(data.get('password'))
    if (Users.objects.filter(name=name,password=password)):
        return render(request, "signIn.html", {})

    
    URLs_List = Dashbord.objects.all()
    print(URLs_List)
    # URLs_List = [{"title": "title1"},{"title": "title2"},{"title": "title3"},] #Dashbord.objects
    context = {
        'URLs_List': URLs_List,
    }
    return render(request, 'list.html',context)


def index(request):
    print('login/index')
    return render(request, "signIn.html", {})

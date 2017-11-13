from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'post', views.submit, name='submit'),
    url(r'index/', views.index, name='index'),
]


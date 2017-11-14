from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'post', views.submit, name='submit'),
    url(r'put', views.submit, name='signup'),
    url(r'', views.index, name='index'),
]


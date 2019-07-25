from django.conf.urls import url
from userdetails import views

urlpatterns = [
    url(r'^first/', views.homePage, name="home"),
    url(r'^second/', views.homeLocation, name="home"),
    url(r'^$', views.pageEmployee)

]



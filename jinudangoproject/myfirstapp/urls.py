from django.conf.urls import url
from myfirstapp import views
urlpatterns = [

   # url(r'^$', views.homePage),

    url(r'^index', views.index,name='index'),

]

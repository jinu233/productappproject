from django.conf.urls import url
from newapp import views
urlpatterns = [

    url(r'^$', views.page),

]
from bookApp import views
from django.conf.urls import url
app_name='bookApp'

urlpatterns=[
    url('', views.bookList.as_view(), name='book_list'),
    url('view/<int:pk>',views.book_view.as_view(),name='book_view'),

]






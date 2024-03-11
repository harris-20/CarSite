from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'carapp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/',views.about,name='about'),
    path('carapp/<int:cartype_no>/', views.cardetail, name='cartype_no'),
   # path('carapp/contact_us/',views.contact_us,name='contact_us'),
    path('carapp/vehicles', views.vehicles,name='vehicles'),
    path('carapp/order', views.orderhere, name='order'),
    path('groupdetail/',views.groupdetail, name='groupdetails'),
]
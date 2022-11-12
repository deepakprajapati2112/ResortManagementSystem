from django.contrib import admin
from django.urls import path
from billingsystem import views

urlpatterns = [
   path("",views.index,name='home'),
   path("about",views.about,name='about'),
   path("service",views.service,name='service'),
   path("aboutpayment",views.aboutpayment,name='aboutpayment'),
   path("contact",views.contact,name='contact')
]

from django.urls import path
from .views import *
urlpatterns =[
    path('',index, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('waste/',waste, name='waste'),
    path('security/',security, name='security'),
    path('transport/',transport, name='transport'),
    path('service/',service, name='service'),
    path('subscription/',subscription, name='subscription'),
    path('contactus/',contactUs,name='contactUs'),
    path('video/<str:pk>/',VideoView,name='video'),
]
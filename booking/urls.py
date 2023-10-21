from . import views
from django.urls import path, include
from django.contrib import admin
from booking import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reserve', views.reserve, name='reserve'), 
    path('reservation', views.reservation, name='get')
]

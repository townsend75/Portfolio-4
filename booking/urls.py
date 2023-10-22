from . import views
from django.urls import path, include
from django.contrib import admin
from booking import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.Reservation.as_view(), name='get'),
    path('reserve/', views.reserve, name='reserve'),
    path('get_name/', views.get_name, name='get_name')
]

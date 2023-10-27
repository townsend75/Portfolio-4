from . import views
from django.urls import path, include
from django.contrib import admin
from booking import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.Reservation.as_view(), name='get'),
    path('reserve/', views.reserve, name='reserve'),
    path('reservation/delete/<int:id>/', views.delete, name='delete'),
    path('reservation/update/<int:id>/', views.update, name='update'),
    path('reservation/update/upwrite/<int:id>/', views.upwrite, name='upwrite')
    ]

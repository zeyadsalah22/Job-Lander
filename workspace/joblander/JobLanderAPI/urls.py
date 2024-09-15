from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flot/', views.flot, name='flot'),
]
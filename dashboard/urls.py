from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create_banner/', views.create_banner),
    path('list_banner/', views.list_banner),
    path('create_aboutus/', views.create_aboutus),
    path('list_aboutus/', views.list_aboutus),
    path('create_price/', views.create_price),
    path('list_price/', views.list_price),
    path('create_service/', views.create_service),
    path('list_service/', views.list_service),
]
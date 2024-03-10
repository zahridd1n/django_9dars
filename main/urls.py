from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.service, name='services')

]

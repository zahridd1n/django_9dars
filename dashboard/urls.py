from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_banner/', views.create_banner, name='create_banner'),
    path('list_banner/', views.list_banner, name='list_banner'),
    path('detail_banner/<int:id>/', views.detail_banner, name='detail_banner'),
    path('edit_banner/<int:id>/', views.edit_banner, name='edit_banner'),
    path('delete_banner/<int:id>/', views.delete_banner, name='delete_banner'),
    path('create_aboutus/', views.create_aboutus, name='create_aboutus'),
    path('list_aboutus/', views.list_aboutus, name='list_aboutus'),
    path('detail_aboutus/<int:id>/', views.detail_aboutus, name='detail_aboutus'),
    path('edit_aboutus/<int:id>/', views.edit_aboutus, name='edit_aboutus'),
    path('delete_aboutus/<int:id>/', views.delete_aboutus, name='delete_aboutus'),
    path('create_price/', views.create_price, name='create_price'),
    path('list_price/', views.list_price, name='list_price'),
    path('detail_price/<int:id>/', views.detail_price, name='detail_price'),
    path('edit_price/<int:id>/', views.edit_price, name='edit_price'),
    path('delete_price/<int:id>/', views.delete_price, name='delete_price'),
    path('create_service/', views.create_service, name='create_service'),
    path('list_service/', views.list_service, name='list_service'),
    path('detail_service/<int:id>/', views.detail_service, name='detail_service'),
    path('edit_service/<int:id>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    path('list_contacts', views.list_contact, name='list_contacts'),
    path('detail_contact/<int:id>/', views.detail_contact, name='detail_contact'),
    path('edit_contact/<int:id>/', views.edit_contact, name='edit_contact'),
    #auth
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    # path('profile', views.profile, name='profile'),
    # path('edit_profile', views.edit_profile, name='edit_profile'),
    # path('change_password', views.change_password, name='change_password'),

    path('q', views.query, name='query'),
]
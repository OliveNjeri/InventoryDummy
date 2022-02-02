from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'dashboard-home' ),
    path('staff/', views.staff, name = 'dashboard-staff'),
    path('products/', views.products, name = 'dashboard-products'),
    path('order/', views.order, name = 'dashboard-order')

]
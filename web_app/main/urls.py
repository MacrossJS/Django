from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('inventory', views.inventory, name='inv'),
    path('about', views.about, name='about'),
]

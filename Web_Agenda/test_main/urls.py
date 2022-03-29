from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('items', views.view_itens, name='view_itens'),
    path('add_item', views.add_item, name='add_item'),

]

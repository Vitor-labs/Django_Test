from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('items', views.view_itens, name='view_itens'),
    path('add_item', views.add_item, name='add_item'),
    path('edit_item', views.edit_item, name='edit_item'),
]

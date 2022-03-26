from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/<int:id>', views.view_itens, name='view_itens'),

]

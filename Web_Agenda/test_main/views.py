from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(request):
    return HttpResponse(
        "<h1> Hello, world. You're at the main index. </h1>" +
        "<h2> This is a test project for learning more aboult Django. </h2>"
    )


def view_itens(request, id):
    todos = ToDoList.objects.get(id=id)
    items = todos.item_set.all()

    return HttpResponse(
        "<h2> You're viewing the items of the list with id: " + str(id) + "</h2>" +
        "<h3> %s </h3>" % todos.name +

        "<h3> %s </h3>" % items
    )

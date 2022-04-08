from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm, ToDoForm
from .models import ToDoList, Item

# Create your views here.

MSG = """
This is a test page for the Django framework.
"""


def home(request):
    return render(request, 'test_main/home.html', {"message": MSG})


def view_itens(request):
    todos = ToDoList.objects.all()

    if request.method == "POST":
        print(request.POST)

    return render(request, 'test_main/lists.html', {"lists": todos})


def add_item(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)

        if form.is_valid():
            nm = form.cleaned_data["todo_text"]
            todo = ToDoList(name=nm)
            todo.save()
            return redirect('/items')
    else:
        form = ToDoForm()
        return render(request, 'test_main/create.html', {"form": form})

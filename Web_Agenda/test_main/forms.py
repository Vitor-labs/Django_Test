from django import forms

from .models import Item, ToDoList


class ItemForm(forms.Form):
    item_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your item',
                'aria-label': 'Item',
                'aria-describedby': 'add-btn',
            }
        )
    )
    check = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'aria-label': 'Checkbox',
                'aria-describedby': 'check-btn',
            }
        )
    )

    class Meta:
        model = Item
        fields = ('item_text',
                  'check')


class ToDoForm(forms.Form):
    list_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your List Name',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )

    create_list = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'btn btn-primary',
                'type': 'submit',
                'value': 'OK',
                'aria-label': 'Create',
                'aria-describedby': 'add-btn',
            }
        )
    )

    class Meta:
        model = ToDoList
        fields = ('list_name',
                  'create_list',)

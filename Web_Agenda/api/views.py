from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response('Hello there')


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request, pk):
    note = Note.objects.get(id=pk)
    if not note:
        return Response('Note not found', status=404)

    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

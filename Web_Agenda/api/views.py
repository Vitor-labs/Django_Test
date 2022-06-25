from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer


# Create your views here.
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


@api_view(['POST'])
def create_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    if not note:
        return Response('Note not found', status=404)

    note.delete()
    return Response('Note deleted')

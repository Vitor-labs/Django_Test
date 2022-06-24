from rest_framework.serializers import ModelSerializer

from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','content', 'created', 'updated']
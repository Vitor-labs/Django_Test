from django.db import models

# Create your models here.


class Note(models.Model):
    content = models.TextField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

from django import forms
from .models import Album, Note

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "artist",
            "year",
            # "created_at",
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "album_note",
        ]
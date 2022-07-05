from django import forms
from .models import Album, Note

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "cover",
            "artist",
            "year",
            "favorite"
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "album_note",
        ]

from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView

from django.shortcuts import render
from .models import Album, Note
from .forms import AlbumForm, NoteForm

# Create your views here.

def list_albums(request):
    albums = Album.objects.all()
    notes = Note.objects.filter()

    return render(request, "junietunes/list_albums.html", {"albums": albums, "notes": notes})

def add_album(request):
    if request.method == "GET":
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(to="list_albums")
    return render(request, "junietunes/add_album.html", {"form": form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")
    return render(request, "junietunes/edit_album.html", {"form": form, "album": album})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "junietunes/album_detail.html", {"album": album})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect(to="list_albums")
    return render(request, "junietunes/delete_album.html", {"album": album})


def add_note(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save()
            new_note.album = album
            new_note.save()
            return redirect(to="album_detail", pk=pk)
    return render(request, "junietunes/note_form.html", {"album": album, "form": form})


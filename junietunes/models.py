from django.db import models
import datetime

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    artist = models.CharField(max_length=255)
    year = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Note(models.Model):
    album_note = models.TextField(blank=True, null=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="album_note", blank=True, null=True)

    def __str__(self):
        return f'{self.album_note}'
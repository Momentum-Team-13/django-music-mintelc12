# Generated by Django 4.0.5 on 2022-06-30 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junietunes', '0002_album_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_note', to='junietunes.album'),
        ),
    ]

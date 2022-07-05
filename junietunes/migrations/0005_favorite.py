# Generated by Django 4.0.5 on 2022-07-04 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junietunes', '0004_album_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_favorite', models.BooleanField(default=False)),
                ('favorite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_button', to='junietunes.favorite')),
            ],
        ),
    ]
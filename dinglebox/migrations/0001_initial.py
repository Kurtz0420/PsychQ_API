# Generated by Django 2.2.6 on 2020-01-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('custom_ordering', models.IntegerField(default=0)),
                ('title', models.CharField(help_text='Name of the Track', max_length=120, unique=True)),
                ('description', models.CharField(blank=True, help_text='Brief description (if any)', max_length=1300, null=True)),
                ('audio_link', models.CharField(help_text='link of the track', max_length=1300)),
                ('thumb_small', models.CharField(blank=True, help_text='Link of small image', max_length=1300, null=True)),
                ('thumb_large', models.CharField(blank=True, help_text='Link of a bit large image', max_length=1300, null=True)),
                ('have_ad', models.BooleanField(default=False, help_text='Will it contain ad')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
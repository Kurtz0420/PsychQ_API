# Generated by Django 2.2.6 on 2019-12-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('custom_ordering', models.IntegerField(default=0)),
                ('title', models.CharField(help_text='Name of the Post', max_length=120, unique=True)),
                ('description', models.CharField(blank=True, help_text='Brief description', max_length=1300, null=True)),
                ('article_content', models.CharField(help_text='Content Of Article Goes Here', max_length=10000)),
                ('parent_course', models.CharField(help_text='Course Name the article belongs to', max_length=100)),
                ('thumbnail', models.CharField(help_text='Thumbnail Slug of the image', max_length=1000, null=True)),
                ('full_res_image', models.CharField(help_text='High Resolution Slug of the image - maybe from pixabay', max_length=1000, null=True)),
                ('universal_count', models.IntegerField(help_text='Count of article in Overall courses')),
                ('course_count', models.IntegerField(help_text='Count of article in its parent course')),
                ('tags', models.CharField(blank=True, help_text='Significant words used in article for search', max_length=1000, null=True)),
                ('reads', models.IntegerField()),
                ('downloads', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

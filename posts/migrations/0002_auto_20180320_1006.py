# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='audio_file_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='posts',
            name='blog_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='posts',
            name='chat_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image_file_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='posts',
            name='video_file_id',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
        migrations.DeleteModel(
            name='Chats',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]

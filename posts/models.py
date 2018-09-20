# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    POST_TYPE_CHOICES = (
    ('TXT', 'text'),
    ('PIC', 'photo'),
    ('QUO', 'quote'),
    ('LINK', 'link'),
    ('AUD', 'audio'),
    ('VID', 'video')
)

    POST_STATUS_CHOICES = (
    ('PUB', 'published'),
    ('DRA', 'draft'),
    ('SCH', 'scheduled'),
    ('PRE', 'preview')
)
    # blog_id = models.ForeignKey('Blogs', on_delete=models.CASCADE)
    # chat_id = models.ForeignKey('Chats', on_delete=models.CASCADE)
    # audio_file_id = models.ForeignKey('Audio', on_delete=models.CASCADE)
    # video_file_id = models.ForeignKey('Video', on_delete=models.CASCADE)
    # image_file_id = models.ForeignKey('Images', on_delete=models.CASCADE)

    blog_id = models.CharField(max_length= 10)
    chat_id = models.CharField(max_length= 10)
    audio_file_id = models.CharField(max_length= 10)
    video_file_id = models.CharField(max_length= 10)
    image_file_id = models.CharField(max_length= 10)
    user_id = models.IntegerField()
    title = models.CharField(max_length= 100)
    body = models.TextField()
    quote_text = models.CharField(max_length= 100)
    quote_source = models.TextField(max_length= 50)
    link_url = models.CharField(max_length= 250)
    link_title = models.TextField(max_length= 50)
    link_caption = models.TextField(max_length= 50)
    post_status = models.CharField(max_length = 20,  choices = POST_STATUS_CHOICES,  default = "DRA")
    post_type = models.CharField(max_length = 20, choices = POST_TYPE_CHOICES, default = "PIC" )
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Posts"   
    





# class Chats(models.Model):
#      chat_id = models.IntegerField()
#      chat_title = models.TextField(max_length= 150)
#      chat_body = models.TextField(max_length= 550)
#      created_at = models.DateTimeField(default = datetime.now, blank = True)
#      updated_at = models.DateTimeField(auto_now=True)
   


# class Audio(models.Model):
#     audio_file_id = models.IntegerField()
#     audio_external_link = models.CharField(max_length= 250)
#     created_at = models.DateTimeField(default = datetime.now, blank = True)
#     updated_at = models.DateTimeField(auto_now=True)
   


# class Video(models.Model):
#     video_file_id = models.IntegerField()
#     video_embed_code = models.CharField(max_length= 250)
#     created_at = models.DateTimeField(default = datetime.now, blank = True)
#     updated_at = models.DateTimeField(auto_now=True)
   

# class Images(models.Model):
#     image_file_id = models.IntegerField()
#     image_url = models.CharField(max_length = 250)
#     caption = models.CharField(max_length = 100)
#     created_at = models.DateTimeField(default = datetime.now, blank = True)
#     updated_at = models.DateTimeField(auto_now=True)
   



# class Blogs(models.Model):
#      blog_id = models.IntegerField()
#      owner_id = models.IntegerField()
#      title = models.CharField(max_length = 50)
#      handle = models.IntegerField()
#      is_private = models.IntegerField()
#      password = models.IntegerField()
#      created_at = models.DateTimeField(default = datetime.now, blank = True)
#      updated_at = models.DateTimeField(auto_now=True)
   

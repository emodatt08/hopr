# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Images(models.Model):


    IMAGE_TYPE = (
            ('GIF', 'gif'),
            ('JPG', 'jpeg'),
            ('PNG', 'png'),
            
    )
  
    image_file_id = models.IntegerField()
    image_url = models.CharField(max_length = 250)
    caption = models.CharField(max_length = 20, choices = IMAGE_TYPE, default = "PNG")
    image_type = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    updated_at = models.DateTimeField(auto_now=True)
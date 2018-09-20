# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Images

# Create your views here.

'''
Returns the index page of images
@param request
@return view
'''
def index(request):
    images = Images.objects.all()[:10]
    return render(request, 'images/index.html', {'images':images})

'''
Returns a format for data
@param dataOb
@return dictionary 'context'
'''
def dataObject(dataOb):
    context = {
        'data':dataOb
    }
    return context

'''
Returns the details page of an image
@param request
@return view
'''
def imageDetails(request, id):
    image = Images.objects.get(id = id)
    return render(request, 'images/details.html', {'image':dataObject(image)})
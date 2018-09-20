# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts



# Bootstrap with index(redirects to the index.html).
def index(request):
    posts = Posts.objects.all()[:10]
    return render(request, 'posts/index.html', {'posts': posts})


def details(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'posts/details.html', {'post': post})



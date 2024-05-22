from django.shortcuts import render
from django.utils import timezone
from . import models

def index(request):
  posts = models.Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "blog/index.html", {"posts": posts})
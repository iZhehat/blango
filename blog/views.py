from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . import models

def index(request):
  posts = models.Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
  post = get_object_or_404(models.Post, slug=slug)
  return render(request, "blog/post-detail.html", {"post": post})
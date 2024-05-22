from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
from django.shortcuts import redirect

from . import models, forms

def index(request):
  posts = models.Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
  post = get_object_or_404(models.Post, slug=slug)
  if request.user.is_active:
    if request.method == "POST":
      comment_form = forms.CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)
    else:
      comment_form = forms.CommentForm
  else:
    comment_form = None
  return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})
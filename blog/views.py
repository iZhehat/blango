from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)

from . import models, forms

def index(request):
  posts = models.Post.objects.filter(published_at__lte=timezone.now()).select_related("author").only("title", "summary", "content", "author", "published_at", "slug")
  logger.debug("Got %d posts", len(posts))
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
        logger.info("created comment on Post %d for user %s", post.pk, request.user)
        return redirect(request.path_info)
    else:
      comment_form = forms.CommentForm
  else:
    comment_form = None
  return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})

def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])
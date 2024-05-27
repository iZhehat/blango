from django.urls import path
import blog.views

urlpatterns = [
  path("", blog.views.index, name='blog_index'),
  path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
  path("ip/", blog.views.get_ip)
]
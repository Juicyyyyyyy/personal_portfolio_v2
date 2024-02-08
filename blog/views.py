from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post

import markdown


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.content = markdown.markdown(post.content)
    return render(request, 'blog/post_detail.html', {'post': post})

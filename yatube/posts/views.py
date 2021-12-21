from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Home page
def index(request):
    # Get posts order by pub, take 10
    posts: dict = Post.objects.order_by('-pub_date')[:10]
    context: dict = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Groups page
def group_posts(request, slug):
    # get_object_or_404
    group: Any = get_object_or_404(Group, slug=slug)
    # Get posts, filter by group, order by pub, take 10
    posts: dict = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context: dict = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

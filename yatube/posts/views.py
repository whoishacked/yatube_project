from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Posts on page quantity constant
POSTS_QUANTITY: int = 10


# Home page
def index(request):
    # Get posts order by pub
    posts: dict = Post.objects.select_related('group').all()[:POSTS_QUANTITY]
    context: dict = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Groups page
def group_posts(request, slug):
    # get_object_or_404
    group: Any = get_object_or_404(Group, slug=slug)
    # Get posts, filter by group, order by pub
    posts: dict = group.posts.all()[:POSTS_QUANTITY]
    context: dict = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

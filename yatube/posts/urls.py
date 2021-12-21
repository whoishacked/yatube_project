# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Home page
    path('', views.index, name='index_page'),
    # Groups
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
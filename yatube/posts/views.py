# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница с группами
def group_posts(request, slug):
    return HttpResponse(f'Группа с slug: {slug}')
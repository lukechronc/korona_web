from django.shortcuts import render
from .models import Post

posts = [
    {
        'author' : 'Luke Chronc',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'March 28, 2020'
    },
    {
        'author': 'Owo Uwu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 29, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'OwO'})
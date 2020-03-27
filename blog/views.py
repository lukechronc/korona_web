from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h>Blog Home</h1>')
    
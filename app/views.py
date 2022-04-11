from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the song index.")

# def indexartist(request):
#     return HttpResponse("Hello, world. You're at the artist index.")

# def indexalbum(request):
#     return HttpResponse("Hello, world. You're at the album index.")
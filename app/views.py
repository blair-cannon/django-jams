from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Artist, Album, Songs


def index(request):
    data = {}
    allsongs = Songs.objects.all().values()
    data['songs'] = list(allsongs)
    return JsonResponse(data)

def artistview(request):
    data = {}
    artists = Artist.objects.all().values()
    data['artists'] = list(artists)
    return JsonResponse(data)

def albumview(request):
    data = {}
    albums = Album.objects.all().values()
    data['albums'] = list(albums)
    return JsonResponse(data)

def singlesong(request, id):
    data = {}
    listsongs = Songs.objects.get(id = id)
    onesong = list(listsongs)
    return JsonResponse(onesong[0])
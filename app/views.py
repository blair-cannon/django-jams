from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *


def index(request):
    data = {}
    allsongs = Songs.objects.all().values()
    data['songs'] = list(allsongs)
    return JsonResponse(data)


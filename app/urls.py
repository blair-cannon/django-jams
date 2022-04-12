from django.urls import path
from .views import index

urlpatterns = [
    path('', index, views.index)
    # path('/artist', views.indexartist, name='artist'),
    # path('/album', views.indexalbum, name='album')
]
from django.urls import path
from .views import index, artistview, albumview, singlesong

urlpatterns = [
    path('', views.index),
    path('', views.artistview),
    path('', views.albumview),
    path('', views.singlesong)
]
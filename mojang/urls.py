from django.urls import path

from . import views

urlpatterns = [
    path('player/<str:player>', views.get_player, name='mojang_get_player'),
]
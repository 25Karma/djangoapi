from django.urls import path

from . import views

urlpatterns = [
    path('player/<str:player>', views.mojang_player_endpoint, name='mojang_player_endpoint'),
]
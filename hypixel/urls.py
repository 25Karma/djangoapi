from django.urls import path

from . import views

urlpatterns = [
    path('friends/<str:uuid>', views.get_friends, name='hypixel_get_friends'),
    path('player/<str:uuid>', views.get_player, name='hypixel_get_player'),
    path('status/<str:uuid>', views.get_status, name='hypixel_get_status'),
]
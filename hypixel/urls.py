from django.urls import path

from . import views

urlpatterns = [
    path('friends/<str:uuid>', views.hypixel_friends_endpoint, name='hypixel_friends_endpoint'),
    path('player/<str:uuid>', views.hypixel_player_endpoint, name='hypixel_player_endpoint'),
    path('guild/<str:uuid>', views.hypixel_guild_endpoint, name='hypixel_guild_endpoint'),
    path('status/<str:uuid>', views.hypixel_status_endpoint, name='hypixel_status_endpoint'),
]
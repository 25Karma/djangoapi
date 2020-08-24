from django.urls import path

from . import views

urlpatterns = [
    path('stats/<str:slug>', views.player_stats_endpoint, name='player_stats_endpoint'),
]
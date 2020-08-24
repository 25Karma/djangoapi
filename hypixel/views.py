from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import hypixel.utilities as utils


# Create your views here.

def hypixel_player_endpoint(request, uuid):
	if request.method == 'GET':
		return JsonResponse(utils.get_player(uuid))

def hypixel_status_endpoint(request, uuid):
	if request.method == 'GET':
		return JsonResponse(utils.get_status(uuid))

def hypixel_friends_endpoint(request, uuid):
	if request.method == 'GET':
		return JsonResponse(utils.get_friends(uuid))

def hypixel_guild_endpoint(request, uuid):
	if request.method == 'GET':
		return JsonResponse(utils.get_guild(uuid))
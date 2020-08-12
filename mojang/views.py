from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import requests

# Create your views here.

def get_player(request, player):
	if (request.method == 'GET'):
		r = requests.get('https://api.ashcon.app/mojang/v2/user/{player}'.format(player=player))
		json = dict(r.json())

	if r.status_code == 200:
		return JsonResponse({
			'success' : True,
			'username': json['username'],
			'uuid'    : json['uuid'],
			})

	if r.status_code == 400:
		return JsonResponse({
			'success' : False,
			'reason' : 'MOJANG_CALL_FAILED',
			'player' : player,
			})

	if r.status_code == 404:
		return JsonResponse({
			'success' : False,
			'reason' : 'MOJANG_PLAYER_DNE',
			'player' : player,
			})
		
	return JsonResponse({'success' : False})
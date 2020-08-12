from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import requests
import os
from dotenv import load_dotenv

# Create your views here.

load_dotenv()
KEY=os.getenv('HYPIXEL_SECRET_KEY')

def default_responses(request):
	if request.status_code == 403:
		return JsonResponse({
			'success' : False,
			'reason' : 'HYPIXEL_ACCESS_DENIED',
			'cause' : json['cause'],
			'uuid' : uuid,
			})

	if request.status_code >= 500:
		return JsonResponse({
			'success' : False,
			'reason' : 'HYPIXEL_API_DOWN',
			})

	return JsonResponse({'success' : False})

def get_player(request, uuid):
	if request.method == 'GET':
		r = requests.get('https://api.hypixel.net/player?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
		json = dict(r.json())

	if r.status_code == 200:
		if json['player'] != None:
			return JsonResponse(json)
		else:
			return JsonResponse({
				'success' : False,
				'reason' : 'HYPIXEL_PLAYER_DNE',
				'uuid' : uuid,
				})

	return default_responses(r)

def get_status(request, uuid):
	if request.method == 'GET':
		r = requests.get('https://api.hypixel.net/status?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
		json = dict(r.json())

	if r.status_code == 200:
		return JsonResponse(json)

	return default_responses(r)

def get_friends(request, uuid):
	if request.method == 'GET':
		r = requests.get('https://api.hypixel.net/friends?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
		json = dict(r.json())

	if r.status_code == 200:
		return JsonResponse(json)

	return default_responses(r)

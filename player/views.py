import requests
import json
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from ratelimit.decorators import ratelimit
import player.utilities as utils

# Create your views here.

@ratelimit(key='ip', rate='12/m', block=True)
def player_stats_endpoint(request, slug):
	if (request.method == 'GET'):
		successful_json = {'success' : True, 'slug' : slug}
		failed_json = {'success' : False, 'slug' : slug}

		# Make call to Mojang API
		mojang_response = requests.get(utils.mojang_endpoint(slug))
		if mojang_response.status_code == 200:
			mojang_json = mojang_response.json()
			successful_json['mojang'] = {
				'username': mojang_json.get('username'),
				'uuid'    : mojang_json.get('uuid'),
			}
		elif mojang_response.status_code == 400:
			failed_json['reason'] = 'MOJANG_CALL_FAILED'
			return JsonResponse(failed_json)
		elif mojang_response.status_code == 404:
			failed_json['reason'] = 'MOJANG_PLAYER_DNE';
			return JsonResponse(failed_json)			
		else:
			failed_json['reason'] = 'UNKNOWN'
			return JsonResponse(failed_json)

		# Make call to Hypixel API
		uuid = successful_json.get('mojang').get('uuid')
		player_response = requests.get(utils.player_endpoint(uuid))
		status_response = requests.get(utils.status_endpoint(uuid))
		friends_response = requests.get(utils.friends_endpoint(uuid))
		guild_response = requests.get(utils.guild_endpoint(uuid))
		if player_response.status_code == 200:
			player_json = player_response.json()
			if player_json.get('player') != None:
				successful_json['player'] = utils.reduce_player(player_json)
			else:
				failed_json['reason'] = 'HYPIXEL_PLAYER_DNE'
				return JsonResponse(failed_json)
		elif player_response.status_code == 403:
			failed_json['reason'] = 'HYPIXEL_ACCESS_DENIED'
			return JsonResponse(failed_json)
		elif player_response.status_code >= 500:
			failed_json['reason'] = 'HYPIXEL_API_DOWN'
			return JsonResponse(failed_json)
		else:
			failed_json['reason'] = 'UNKNOWN'
			return failed_json
		successful_json['status'] = status_response.json().get('session')
		successful_json['friends'] = utils.reduce_friends(friends_response.json())
		successful_json['guild'] = utils.reduce_guild(guild_response.json())
		return JsonResponse(successful_json)
import json
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from ratelimit.decorators import ratelimit
import mojang.utilities as mojang_utils
import hypixel.utilities as hypixel_utils

# Create your views here.

@ratelimit(key='ip', rate='20/m', block=True)
def player_stats_endpoint(request, slug):
	if (request.method == 'GET'):
		mojang = mojang_utils.get_player(slug)
		if (mojang.get('success') == True):
			friends = hypixel_utils.get_friends(mojang.get('uuid'))
			guild = hypixel_utils.get_guild(mojang.get('uuid'))
			player = hypixel_utils.filter_player(hypixel_utils.get_player(mojang.get('uuid')))
			status = hypixel_utils.get_status(mojang.get('uuid'))
		return JsonResponse({
			'mojang' : mojang,
			'friends': friends,
			'guild'  : guild,
			'player' : player,
			'status' : status,
			})
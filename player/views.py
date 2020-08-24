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
		# If the player does not exist or the call failed
		if (mojang.get('success') == False):
			return JsonResponse(mojang)
		uuid = mojang.get('player').get('uuid')
		player = hypixel_utils.reduce_player(hypixel_utils.get_player(uuid))
		# If the player has never played on Hypixel or the call failed
		if (player.get('success') == False):
			return JsonResponse(player)
		# I assume that if getting Hypixel player is successful, then the others will also be fine
		friends = hypixel_utils.reduce_friends(hypixel_utils.get_friends(uuid))
		guild = hypixel_utils.reduce_guild(hypixel_utils.get_guild(uuid))
		status = hypixel_utils.get_status(uuid)
		return JsonResponse({
			'success': True,
			'mojang' : mojang.get('player'),
			'friends': friends.get('friendCount'),
			'guild'  : guild.get('guild'),
			'player' : player.get('player'),
			'status' : status.get('session'),
		})
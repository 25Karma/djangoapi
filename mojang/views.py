from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
import mojang.utilities as utils

# Create your views here.

def mojang_player_endpoint(request, player):
	if (request.method == 'GET'):	
		return JsonResponse(utils.get_player(player))


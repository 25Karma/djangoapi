from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

def ratelimited_endpoint(request, exception):
	return JsonResponse({
		'success': False,
		'reason': 'RATELIMITED',
		})
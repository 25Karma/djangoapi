import requests
import os
from dotenv import load_dotenv
from hypixel.filter import player_filter

load_dotenv()
KEY = os.getenv('HYPIXEL_SECRET_KEY')

def failed_responses(response):
	json = response.json()
	if response.status_code == 403:
		return {
			'success' : False,
			'reason' : 'HYPIXEL_ACCESS_DENIED',
			'cause' : json.get('cause'),
			}

	if response.status_code >= 500:
		return {
			'success' : False,
			'reason' : 'HYPIXEL_API_DOWN',
			}
	return {
		'success' : False,
		'reason' : 'UNKNOWN',
	}

# These functions make the calls to the Hypixel API, 
# and directly return the data it receives

def get_player(uuid):
	response = requests.get('https://api.hypixel.net/player?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
	json = dict(response.json())
	if response.status_code == 200:
		if json.get('player') != None:
			return json
		else:
			return {
				'success' : False,
				'reason' : 'HYPIXEL_PLAYER_DNE',
				}
	return failed_responses(response)

def get_status(uuid):
	response = requests.get('https://api.hypixel.net/status?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
	json = dict(response.json())
	if response.status_code == 200:
		return json
	return failed_responses(response)

def get_friends(uuid):
	response = requests.get('https://api.hypixel.net/friends?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid))
	json = dict(response.json())
	if response.status_code == 200:
		return json
	return failed_responses(response)

def get_guild(uuid):
	response = requests.get('https://api.hypixel.net/guild?key={key}&player={uuid}'.format(key=KEY, uuid=uuid))
	json = dict(response.json())
	if response.status_code == 200:
		return json
	return failed_responses(response)
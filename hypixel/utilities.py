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

# These functions are for reducing the size of the JSON before we send it over

def reduce_player(json):
	raw_player_data = json.get('player')
	if (json.get('success') == True and raw_player_data != None):
		return {
			'success': True,
			'player' : {
				key: raw_player_data.get(key) for key in player_filter if raw_player_data.get(key) != None
			},
		}
	return json

def reduce_friends(json):
	raw_friends_data = json.get('records')
	if (json.get('success') == True and raw_friends_data != None):
		return {
			'success': True,
			'friendCount' : len(raw_friends_data),
		}
	return json


def reduce_guild(json):
	guild = json.get('guild')
	if (json.get('success') == True and guild != None):
		guild['members'] = len(guild.get('members'))
		return {
			'success': True,
			'guild' : guild,
		}
	return json
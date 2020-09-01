import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('HYPIXEL_SECRET_KEY')
def mojang_endpoint(slug):
	return 'https://api.ashcon.app/mojang/v2/user/{slug}'.format(slug=slug)
def player_endpoint(uuid):
	return 'https://api.hypixel.net/player?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid)
def status_endpoint(uuid):
	return 'https://api.hypixel.net/status?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid)
def friends_endpoint(uuid):
	return 'https://api.hypixel.net/friends?key={key}&uuid={uuid}'.format(key=KEY, uuid=uuid)
def guild_endpoint(uuid):
	return 'https://api.hypixel.net/guild?key={key}&player={uuid}'.format(key=KEY, uuid=uuid)

# These functions are for reducing the size of the JSON before we send it over

player_filter = [
	'achievementPoints',
	'displayname',
	'eulaCoins',
	'firstLogin',
	'karma',
	'knownAliases',
	'lastLogin',
	'lastLogout',
	'monthlyPackageRank',
	'monthlyRankColor',
	'networkExp',
	'newPackageRank',
	'packageRank',
	'petConsumables',
	'petStats',
	'playername',
	'prefix',
	'rank',
	'rankPlusColor',
	'socialMedia',
	'stats',
	'tournamentTokens',
	'tourney',
	'userLanguage',
	'uuid',
]

def reduce_player(json):
	raw_player_data = json.get('player')
	questsCompleted = 0
	if (raw_player_data.get('quests') != None):
		for (key,val) in raw_player_data.get('quests').items():
			if (val.get('completions') != None):
				questsCompleted += len(val.get('completions'))
	player = { key: raw_player_data.get(key) for key in player_filter if raw_player_data.get(key) != None }
	player['questsCompleted'] = questsCompleted
	return player

def reduce_friends(json):
	raw_friends_data = json.get('records')
	if (json.get('success') == True and raw_friends_data != None):
		return len(raw_friends_data)
	else:
		return raw_friends_data


def reduce_guild(json):
	guild = json.get('guild')
	if (json.get('success') == True and guild != None):
		guild['members'] = len(guild.get('members'))
		return guild
	else:
		return guild
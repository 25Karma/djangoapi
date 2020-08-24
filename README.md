# 25Karma API
A Django REST API for [25Karma](https://25karma.github.io).

## Documentation
The root url of the API is [https://karma-25.uc.r.appspot.com](https://karma-25.uc.r.appspot.com/).

### Player
Combines the Mojang and Hypixel endpoints into a single request.  

* Mojang username and UUID
* Abbreviated player stats
* Online status
* Friends
* Guild

| Get          | From             | Endpoint                             |
|--------------|------------------|--------------------------------------|
| Player stats | username or UUID | {root}/player/stats/{username/UUID} |

### Mojang (deprecated)
| Get               | From             | Endpoint                             |
|-------------------|------------------|--------------------------------------|
| username and UUID | username or UUID | {root}/mojang/player/{username/UUID} |

### Hypixel (deprecated)
| Get           | From | Endpoint                      |
|---------------|------|-------------------------------|
| Player stats  | UUID | {root}/hypixel/player/{UUID}  |
| Online status | UUID | {root}/hypixel/status/{UUID}  |
| Friends       | UUID | {root}/hypixel/friends/{UUID} |
| Guild         | UUID | {root}/hypixel/guild/{UUID}   |
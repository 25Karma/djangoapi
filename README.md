# 25Karma API
A Django REST API for [25Karma](https://25karma.github.io).

## Documentation
The root url of the API is [https://karma-25.uc.r.appspot.com](https://karma-25.uc.r.appspot.com/).

### Mojang
| Get               | From             | Endpoint                             |
|-------------------|------------------|--------------------------------------|
| username and UUID | username or UUID | {root}/mojang/player/{username/UUID} |

### Hypixel
| Get           | From | Endpoint                      |
|---------------|------|-------------------------------|
| Player stats  | UUID | {root}/hypixel/player/{UUID}  |
| Online status | UUID | {root}/hypixel/status/{UUID}  |
| Friends       | UUID | {root}/hypixel/friends/{UUID} |
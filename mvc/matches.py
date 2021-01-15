import requests

from APIkey import getApiKey

def matches(matchID):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matches/" + matchID + "?api_key=" + getApiKey()
    dados = requests.get(URL)
    return dados.json()

print(matches('2160416202'))
import requests

from APIkey import getApiKey

def maestriaInvocador(id):
    URL = "https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + \
          id + "?api_key=" + getApiKey()
    dados = requests.get(URL)
    return dados.json()
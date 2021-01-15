import requests

from APIkey import getApiKey

def rankInvocador(id):
    URL = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
          id + "?api_key=" + getApiKey()
    dados = requests.get(URL)
    return dados.json()
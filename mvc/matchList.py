import requests

from APIkey import getApiKey


def matchList(accountID):
    URL = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountID + "?api_key=" + getApiKey()
    dados = requests.get(URL)
    return dados.json()


print(matchList('i0unkXaDiO3VL-oKzzAR2D9XUkx7nak2429kkPk1cFpoaYY'))

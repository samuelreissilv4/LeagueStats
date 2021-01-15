import requests

from APIkey import getApiKey


def dadosInvocador(nome):
    URL = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
        nome + "?api_key=" + getApiKey()
    dados = requests.get(URL)
    return dados.json()


print(dadosInvocador("l edu l"))

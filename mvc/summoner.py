import requests

from APIkey import getApiKey


def dadosInvocador(summoner):
    if summoner != '':
        URL = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
        summoner + "?api_key=" + getApiKey()
        dados = requests.get(URL)
        return dados.json()

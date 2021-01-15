import requests

from APIkey import getApiKey

def champions():
    URL = "http://ddragon.leagueoflegends.com/cdn/11.1.1/data/pt_BR/champion.json"
    dados = requests.get(URL)
    return dados.json()
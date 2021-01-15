import requests

from APIkey import getApiKey

def profileIcons():
    URL =  "http://ddragon.leagueoflegends.com/cdn/11.1.1/data/pt_BR/profileicon.json"
    dados = requests.get(URL)
    return dados.json()
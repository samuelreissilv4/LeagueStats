import requests
from APIkey import getApiKey

APIKey = getApiKey()


def dadosInvocador(nome):
    URL = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
          nome + "?api_key=" + APIKey
    dados = requests.get(URL)
    return dados.json()


def rankInvocador(id):
    URL = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
          id + "?api_key=" + APIKey
    dados = requests.get(URL)
    return dados.json()


if __name__ == '__main__':
    try:
        nome = input("Insira o nome no jogador: ")
        invocador = dadosInvocador(nome)
        print("Jogador:" + invocador['name'])
        rank = rankInvocador(invocador['id'])
        try:
            print("Fila: " + rank[0]['queueType'])
            print("Elo: " + rank[0]['tier'], rank[0]['rank'])
            print("Pontos: " + str(rank[0]['leaguePoints']) + " PDL")
            print("#################################")
            print("Fila: " + rank[1]['queueType'])
            print("Elo: " + rank[1]['tier'], rank[1]['rank'])
            print("Pontos: " + str(rank[1]['leaguePoints']) + " PDL")
        except IndexError as erro:
            print("Jogador nao ranqueado")
    except KeyError as erro:
        print("Jogador nao encontrado")
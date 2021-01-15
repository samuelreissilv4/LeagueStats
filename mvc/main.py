from summoner import dadosInvocador
from ranked import rankInvocador
from mastery import maestriaInvocador

print(dadosInvocador('l edu l'))
print(rankInvocador(dadosInvocador('l edu l')['id']))
print(maestriaInvocador(dadosInvocador('l edu l')['id']))
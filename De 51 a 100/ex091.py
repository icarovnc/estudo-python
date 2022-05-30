from random import randint
from time import sleep
jogador = {}
cont = 0
#criando os jogadores e randomizando os dados
for c in range(1, 5):
    jogador[f'Jogador{c}'] = randint(1, 6)
#mostrando qual valor cada jogador tirou
for k, v in jogador.items():
    print(f'O {k} tirou: {v}')
    sleep(0.7)
#mostrando o ranking de forma ordenada usando sorted
print('-' * 10, 'Ranking', '-' * 10)
for item in sorted(jogador, key=jogador.get, reverse=True):
    cont += 1
    print(f'{cont}° lugar: {item} com {jogador[item]}')
    sleep(0.7)
import random
from time import sleep
print(F'{"ESCOLHA":=^30}')
escolha = int(input('[ 0 ] PEDRA '
                    '\n[ 1 ] PAPEL '
                    '\n[ 2 ] TESOURA'))
joken = ['PEDRA', 'PAPEL', 'TESOURA']
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!')
sleep(0.8)
if escolha == 0: #JOGADOR ESCOLHE PEDRA
    pc = random.choice(joken)
    if pc == joken[0]:
        print('JOGO EMPATE')
    elif pc == joken[1]:
        print('PC VENCE')
    elif pc == joken[2]:
        print('JOGADOR VENCE')
elif escolha == 1: #JOGADOR ESCOLHE PAPEL
    pc = random.choice(joken)
    if pc == joken[0]:
        print('JOGADOR VENCE')
    elif pc == joken[1]:
        print('JOGO EMPATE')
    elif pc == joken[2]:
        print('PC VENCE')
elif escolha == 2: #JOGADOR ESCOLHE TESOURA
    pc = random.choice(joken)
    if pc == joken[0]:
        print('PC VENCE')
    elif pc == joken[1]:
        print('JOGADOR VENCE')
    elif pc == joken[2]:
        print('JOGO EMPATE')

print('-=' * 15)

if escolha == 0: #JOGADOR ESCOLHE PEDRA
    pc = random.choice(joken)
    if pc == joken[0] and pc != joken[1] and pc != joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[0]} '
              f'\nJOGO EMPATE')
    elif pc != joken[0] and pc == joken[1] and pc != joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[0]}'
              f'\nPC VENCEU')
    elif pc != joken[0] and pc != joken[1] and pc == joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[0]}'
              f'\nJOGADOR VENCEU')
elif escolha == 1: #JOGADOR ESCOLHE PAPEL
    pc = random.choice(joken)
    if pc == joken[1] and pc != joken[0] and pc != joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[1]}'
              f'\nJOGO EMPATE')
    elif pc != joken[1] and pc == joken[0] and pc != joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[1]}'
              f'\nJOGADOR VENCE')
    elif pc != joken[1] and pc != joken[0] and pc == joken[2]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[1]}'
              f'\nPC VENCE')
elif escolha == 2: #JOGADOR ESCOLHE TESOURA
    pc = random.choice(joken)
    if pc == joken[2] and pc != joken[0] and pc != joken[1]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[2]}'
              f'\nJOGO EMPATE')
    elif pc != joken[2] and pc == joken[0] and pc != joken[1]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[2]}'
              f'\nPC VENCE')
    elif pc != joken[2] and pc != joken[0] and pc == joken[1]:
        print(f'O PC ESCOLHEU {pc} '
              f'\nO JOGADOR ESCOLHE {joken[2]}'
              f'\nJOGADOR VENCE')
print('-=' * 15)
from random import randint
from time import sleep

nome = input('Qual o seu nome: ').strip()
exercício = randint(1, 50)

print(f'Tudo bem {nome}? Vou escolher um exercício para você revisar.')
input('Digite enter para que eu procure o exercício.')
sleep(0.5)
print('\033[31mEscolhendo...\033[m', end='')
sleep(1)
print('\033[31m3...', end='')
sleep(1)
print('\033[31m2...', end='')
sleep(1)
print('\033[31m1...', end='')
sleep(2)
print('\033[31mAchei!!!\033[m')
sleep(2)
print(f'Você deve revisar o exercício {exercício}!!!')
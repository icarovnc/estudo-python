from random import randint
from time import sleep

pc = randint(0, 100)
pessoa = int(input('Digite um número de 0 a 100: '))
cont = 1
while pc != pessoa:
    pessoa = int(input('Tente novamente: '))
    cont += 1
    if pc == pessoa:
        print(f'Acertou! Você precisou de {cont} tentativas para acertar.')
    else:
        if pessoa > pc:
            print('Tente um número menor')
        elif pessoa < pc:
            print('Tente um número maior')
print('fim')

from random import sample
from time import sleep
lista = []
numeros = []
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, qtd):
    lista = sample(range(1, 60), k=6)
    numeros.append(lista[:])
    lista.clear()
for c in range(0, qtd):
    print(f'{sorted(numeros[c])}', end='')
    sleep(0.5)
    print()
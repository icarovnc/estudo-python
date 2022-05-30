from random import sample

def sorteia():
    lista = (sample(range(1, 10), k=5))
    return lista

def somaPar(lst):
    soma = 0
    print(f'Somando os valores pares da lista {lst}.', end=' ')
    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares é: {soma}')


somaPar(sorteia())
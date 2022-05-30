from time import sleep

def linha():
    print('-=' * 35)


def analisando():
    print('Analisando os valores passados')

def maior (*numeros):
    ordenados = sorted(numeros)
    linha()
    analisando()
    for valor in numeros:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
    print(f'', end='')
    print(f'foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi: {ordenados[-1]}')

maior(1, 2, 5, 6, 7, 8, 9, 55, 33, 45)
maior(50, 66, 100, 25, 152, 1058, 3, 1, 45, 25, 14, 12, 23, 14)
maior(45, 3, 6, 7)
from random import randint
sorteado = tuple(randint(0, 99) for i in range(5))
sorteado = sorted(sorteado)
print(sorteado)
ma = sorted(sorteado[-1:])
me = sorted(sorteado[0:1])
print(f'O maior valor sorteado é {ma}')
print(f'O menor valor sorteado é {me}')


'''a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
tupla = (a, b, c, d)'''
tupla = tuple(int(input('Digite os valores: ')) for c in range(0, 4)) #como iniciar uma tupla em um intervalo
cont = 0
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3):
    print(f'O valor 3 apareceu na posição {tupla.index(3)}')
else:
    print('O valor 3 não foi digitado')

for p in tupla:
    if p % 2 == 0:
        cont += 1
print(f'Os valores pares digitados foram {cont}')
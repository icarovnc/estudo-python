n = int(input('Digite um número: '))
c = n
f = 1
while c != 1:
    f = f * c
    c -= 1
    print(f'{n} X {c} = {f}')
print(f'O valor fatorial de {n} é igual a {f}')
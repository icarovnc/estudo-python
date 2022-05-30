numeros = list()
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    if n in numeros:
        while n in numeros:
            n = int(input('Número duplicado. Digite outro número:'))
    numeros += [n]
    numeros = sorted(numeros)
    numeros.sort()
    print(f'{n} foi adicionado na posição {numeros.index(n)}')
print(f'Os valores digitados em ordem foram {numeros}')

#======================================================================

numero = list()
for a in range(0, 4):
    n = int(input('Digite um valor: '))
    if a == 0 or n > numero[-1]:
        numero.append(n)
    else:
        c =0
        while c < len(numero):
            if c <= numero[c]:
                numero.insert(c, n)
                break
print(f'Os valores digitados em ordem foram {numero}')
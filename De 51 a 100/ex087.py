matriz = [[], [], []]
soma = 0
for c in range(0, 3):
    for n in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {n}]: ')))
for t in range(0, 3):
    for t2 in range(0, 3):
        print(f'[{matriz[t][t2]:^5}]', end='')
        if matriz[t][t2] % 2 == 0:
            soma += matriz[t][t2]
    print()

print('=-' * 20)
print(f'A soma dos valores pares é: {soma}' )
print(f'A soma dos números da terceira coluna é: {sum(matriz[2])}')
print(f'O maior número da segunda linha é: {max(matriz[1])}')
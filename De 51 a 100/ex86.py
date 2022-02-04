matriz = [[], [], []]
soma = 0
for c in range(0, 3):
    for n in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {n}]: ')))
for t in range(0, 3):
    for t2 in range(0, 3):
        print(f'[{matriz[t][t2]:^5}]', end='')
    print()
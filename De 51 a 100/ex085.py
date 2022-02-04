numeros = [[], []]

for c in range(0, 7):
    temp = (int(input(f'{c + 1}° número: ')))
    if temp % 2 == 0:
        numeros[0].append(temp)

    elif temp % 2 == 1:
        numeros[1].append(temp)
print(f'Os valores parrs digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
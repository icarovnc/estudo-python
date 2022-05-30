valores = list()
for c in range(0, 5):
    valores.append(input('Digite os números: '))
print(valores)
print(f'O maior valor foi {max(valores)} e está na posição {valores.index(max(valores))}...', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end='')
print(f'\nO menor valor foi {min(valores)} e está na posição {valores.index(min(valores))}...', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}...', end='')
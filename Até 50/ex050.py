cont = soma = 0
num = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} números pares e a soma deles deu {soma}')
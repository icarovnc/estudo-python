cont = soma = n = 0
while n != 999:
    cont += 1
    n = int(input('Digite um número: '))
    if n == 999:
        print('Programa finalizado')
    else:
        soma += n
print(f'Você digitou {cont - 1} números e a soma dos números é {soma}')
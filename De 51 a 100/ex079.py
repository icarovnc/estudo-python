n = continuar = verificar = list()
cont = a = 0
while True:
    n = int(input('Digite um valor: '))
    if n in verificar:
        print('Valor duplicado! Não vou adicionar')
        verificar.remove(n)
    verificar += [n]
    continuar = str(input('Deseja Continuar? [S/N] ')).strip().lower()
    while continuar not in 'sn':
        print('Opção inválida. ', end='')
        continuar = str(input('Deseja Continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print(f'Você digitou os valores {sorted(verificar)}')